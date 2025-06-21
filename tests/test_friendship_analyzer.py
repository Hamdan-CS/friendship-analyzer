#!/usr/bin/env python3
"""
Unit tests for the Friendship Analyzer

Run with: 
    python -m unittest tests.test_friendship_analyzer
    or
    python tests/test_friendship_analyzer.py
"""

import unittest
import sys
import os

# Add parent directory to path to import main module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import from your main file
from friendship_analyzer import (
    Person, FriendshipAnalyzer, EmpatheticPerson, LogicalPerson, 
    CreativePerson, ReservedPerson, EnergeticPerson, AnalyticalPerson,
    AdventurousPerson, IntrovertPerson, HumorousPerson
)


class TestFriendshipAnalyzer(unittest.TestCase):
    """Complete test suite for the Friendship Analyzer"""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.analyzer = FriendshipAnalyzer()
        
        # Standard test persons
        self.alice = Person(
            "Alice", 25, 
            ["reading", "coding"], 
            {"extroversion": 5, "openness": 7, "agreeableness": 8, "conscientiousness": 6, "neuroticism": 4}, 
            {"direct": 6, "emotional": 8, "humor": 5, "formal": 4}
        )
        
        self.bob = Person(
            "Bob", 27, 
            ["coding", "gaming"], 
            {"extroversion": 6, "openness": 6, "agreeableness": 7, "conscientiousness": 7, "neuroticism": 5}, 
            {"direct": 8, "emotional": 5, "humor": 6, "formal": 5}
        )
        
        self.charlie = LogicalPerson(
            "Charlie", 26, 
            ["chess", "coding"], 
            {"extroversion": 4, "openness": 6, "agreeableness": 7, "conscientiousness": 9, "neuroticism": 3}, 
            {"direct": 9, "emotional": 3, "humor": 4, "formal": 8}
        )

    def test_person_creation(self):
        """Test that Person objects are created correctly"""
        self.assertEqual(self.alice.name, "Alice")
        self.assertEqual(self.alice.age, 25)
        self.assertIn("reading", self.alice.interests)
        self.assertEqual(self.alice.personality_traits["extroversion"], 5)
        self.assertEqual(len(self.alice.friendships), 0)

    def test_add_person_to_analyzer(self):
        """Test adding people to the analyzer"""
        initial_count = len(self.analyzer.people)
        self.analyzer.add_person(self.alice)
        self.assertEqual(len(self.analyzer.people), initial_count + 1)
        self.assertEqual(self.analyzer.people[-1].name, "Alice")

    def test_interest_compatibility_shared_interests(self):
        """Test interest compatibility with shared interests"""
        # Alice: ["reading", "coding"], Bob: ["coding", "gaming"]
        # Shared: 1 (coding), Total: 3 (reading, coding, gaming)
        # Expected: (1/3) * 10 = 3.33
        score = self.analyzer.calculate_interest_compatibility(self.alice, self.bob)
        expected_score = (1/3) * 10
        self.assertAlmostEqual(score, expected_score, places=2)

    def test_interest_compatibility_no_shared_interests(self):
        """Test interest compatibility with no shared interests"""
        person_different = Person("David", 30, ["sports", "music"], {}, {})
        score = self.analyzer.calculate_interest_compatibility(self.alice, person_different)
        expected_score = 0  # No shared interests
        self.assertEqual(score, expected_score)

    def test_interest_compatibility_identical_interests(self):
        """Test interest compatibility with identical interests"""
        person_identical = Person("Eve", 25, ["reading", "coding"], {}, {})
        score = self.analyzer.calculate_interest_compatibility(self.alice, person_identical)
        self.assertEqual(score, 10)  # All interests shared

    def test_interest_compatibility_empty_interests(self):
        """Test interest compatibility when one person has no interests"""
        person_empty = Person("Frank", 25, [], {}, {})
        score = self.analyzer.calculate_interest_compatibility(self.alice, person_empty)
        # Alice has interests, Frank has none, so total > 0, shared = 0
        self.assertEqual(score, 0)

    def test_age_compatibility_calculation(self):
        """Test age compatibility calculation with different age gaps"""
        # Test cases: (age1, age2, expected_score)
        test_cases = [
            (25, 27, 10),  # 2 years diff
            (25, 25, 10),  # Same age
            (25, 30, 8),   # 5 years diff
            (25, 35, 6),   # 10 years diff
            (25, 40, 4),   # 15 years diff
            (25, 45, 2),   # 20 years diff
        ]
        
        for age1, age2, expected in test_cases:
            person1 = Person("Test1", age1, [], {}, {})
            person2 = Person("Test2", age2, [], {}, {})
            score = self.analyzer.calculate_age_compatibility(person1, person2)
            self.assertEqual(score, expected, f"Age diff {abs(age1-age2)} should give score {expected}")

    def test_personality_compatibility_identical_traits(self):
        """Test personality compatibility with identical traits"""
        person_identical = Person("Grace", 25, [], 
                                {"extroversion": 5, "openness": 7, "agreeableness": 8, "conscientiousness": 6, "neuroticism": 4}, 
                                {})
        score = self.analyzer.calculate_personality_compatibility(self.alice, person_identical)
        self.assertEqual(score, 10)  # No differences = perfect score

    def test_personality_compatibility_different_traits(self):
        """Test personality compatibility with different traits"""
        person_opposite = Person("Henry", 25, [], 
                               {"extroversion": 1, "openness": 1, "agreeableness": 1, "conscientiousness": 1, "neuroticism": 1}, 
                               {})
        score = self.analyzer.calculate_personality_compatibility(self.alice, person_opposite)
        # Should be low score due to big differences
        self.assertLess(score, 5)

    def test_communication_compatibility_identical_styles(self):
        """Test communication compatibility with identical styles"""
        person_identical = Person("Iris", 25, [], {}, 
                                {"direct": 6, "emotional": 8, "humor": 5, "formal": 4})
        score = self.analyzer.calculate_communication_compatibility(self.alice, person_identical)
        self.assertEqual(score, 10)  # Identical styles = perfect score

    def test_logical_person_strategy(self):
        """Test LogicalPerson compatibility strategy"""
        # Charlie (LogicalPerson) with Bob (has direct communication)
        score = self.charlie.compatibility_strategy(self.bob)
        self.assertEqual(score, 10)  # Bob has "direct" in communication style

        # Charlie with Alice (doesn't have high direct communication)
        score = self.charlie.compatibility_strategy(self.alice)
        self.assertEqual(score, 3)  # Alice doesn't have high "direct" style

    def test_empathetic_person_strategy(self):
        """Test EmpatheticPerson compatibility strategy"""
        empathetic = EmpatheticPerson("Emma", 28, [], {}, {})
        
        # Test with someone who has emotional communication
        emotional_person = Person("Felix", 30, [], {}, {"emotional": 9})
        score = empathetic.compatibility_strategy(emotional_person)
        self.assertEqual(score, 10)
        
        # Test with someone who doesn't have emotional communication
        non_emotional = Person("George", 30, [], {}, {"direct": 9})
        score = empathetic.compatibility_strategy(non_emotional)
        self.assertEqual(score, 4)

    def test_reserved_person_strategy(self):
        """Test ReservedPerson compatibility strategy"""
        reserved = ReservedPerson("Rachel", 24, [], {}, {})
        
        # Test with introvert (low extroversion)
        introvert = Person("Ian", 25, [], {"extroversion": 3}, {})
        score = reserved.compatibility_strategy(introvert)
        self.assertEqual(score, 9)
        
        # Test with extrovert (high extroversion)
        extrovert = Person("Jack", 25, [], {"extroversion": 8}, {})
        score = reserved.compatibility_strategy(extrovert)
        self.assertEqual(score, 4)

    def test_overall_compatibility_calculation(self):
        """Test overall compatibility calculation"""
        score = self.analyzer.analyze_compatibility(self.alice, self.bob)
        
        # Score should be between 0 and 10
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 10)
        
        # Score should be deterministic (same input = same output)
        score2 = self.analyzer.analyze_compatibility(self.alice, self.bob)
        self.assertEqual(score, score2)

    def test_find_best_matches(self):
        """Test finding best matches functionality"""
        self.analyzer.add_person(self.alice)
        self.analyzer.add_person(self.bob)
        self.analyzer.add_person(self.charlie)
        
        matches = self.analyzer.find_best_matches(self.alice)
        
        # Should return 2 matches (excluding self)
        self.assertEqual(len(matches), 2)
        
        # Matches should be sorted by score (highest first)
        if len(matches) > 1:
            self.assertGreaterEqual(matches[0][1], matches[1][1])
        
        # Each match should be a tuple of (person, score)
        for match in matches:
            self.assertIsInstance(match[0], Person)
            self.assertIsInstance(match[1], (int, float))
            self.assertNotEqual(match[0], self.alice)  # Should not match with self

    def test_create_friendship_network(self):
        """Test friendship network creation"""
        self.analyzer.add_person(self.alice)
        self.analyzer.add_person(self.bob)
        self.analyzer.add_person(self.charlie)
        
        # Set a lower threshold for testing
        self.analyzer.compatibility_threshold = 5.0
        
        self.analyzer.create_friendship_network()
        
        # Check that friendships were created
        for person in self.analyzer.people:
            for friendship in person.friendships:
                self.assertIn('friend', friendship)
                self.assertIn('compatibility_score', friendship)
                self.assertGreaterEqual(friendship['compatibility_score'], 5.0)

    def test_empty_analyzer_edge_cases(self):
        """Test analyzer with no people"""
        empty_analyzer = FriendshipAnalyzer()
        matches = empty_analyzer.find_best_matches(self.alice)
        self.assertEqual(len(matches), 0)

    def test_single_person_analyzer(self):
        """Test analyzer with only one person"""
        single_analyzer = FriendshipAnalyzer()
        single_analyzer.add_person(self.alice)
        matches = single_analyzer.find_best_matches(self.alice)
        self.assertEqual(len(matches), 0)

    def test_compatibility_score_ranges(self):
        """Test that all compatibility scores are within expected ranges"""
        test_people = [self.alice, self.bob, self.charlie]
        
        for i, person1 in enumerate(test_people):
            for person2 in test_people[i+1:]:
                # Test individual components
                interest_score = self.analyzer.calculate_interest_compatibility(person1, person2)
                self.assertGreaterEqual(interest_score, 0)
                self.assertLessEqual(interest_score, 10)
                
                personality_score = self.analyzer.calculate_personality_compatibility(person1, person2)
                self.assertGreaterEqual(personality_score, 0)
                self.assertLessEqual(personality_score, 10)
                
                age_score = self.analyzer.calculate_age_compatibility(person1, person2)
                self.assertGreaterEqual(age_score, 0)
                self.assertLessEqual(age_score, 10)
                
                # Test overall score
                overall_score = self.analyzer.analyze_compatibility(person1, person2)
                self.assertGreaterEqual(overall_score, 0)
                self.assertLessEqual(overall_score, 10)

    def test_symmetry_of_base_compatibility_metrics(self):
        """Test if base compatibility calculations are symmetric"""
        # Interest compatibility should be symmetric
        score1 = self.analyzer.calculate_interest_compatibility(self.alice, self.bob)
        score2 = self.analyzer.calculate_interest_compatibility(self.bob, self.alice)
        self.assertEqual(score1, score2)
        
        # Age compatibility should be symmetric
        age_score1 = self.analyzer.calculate_age_compatibility(self.alice, self.bob)
        age_score2 = self.analyzer.calculate_age_compatibility(self.bob, self.alice)
        self.assertEqual(age_score1, age_score2)
        
        # Personality compatibility should be symmetric
        personality_score1 = self.analyzer.calculate_personality_compatibility(self.alice, self.bob)
        personality_score2 = self.analyzer.calculate_personality_compatibility(self.bob, self.alice)
        self.assertEqual(personality_score1, personality_score2)

    def test_different_person_types(self):
        """Test different person type strategies"""
        # Create different person types
        creative = CreativePerson("Creative", 25, [], {"openness": 8}, {"humor": 8})
        energetic = EnergeticPerson("Energetic", 25, [], {"extroversion": 9}, {})
        analytical = AnalyticalPerson("Analytical", 25, [], {"conscientiousness": 8}, {})
        
        # Test their strategies work
        self.assertIsInstance(creative.compatibility_strategy(self.alice), (int, float))
        self.assertIsInstance(energetic.compatibility_strategy(self.alice), (int, float))
        self.assertIsInstance(analytical.compatibility_strategy(self.alice), (int, float))

    def test_display_network_stats(self):
        """Test network statistics display (doesn't crash)"""
        self.analyzer.add_person(self.alice)
        self.analyzer.add_person(self.bob)
        self.analyzer.create_friendship_network()
        
        # This should not raise an exception
        try:
            self.analyzer.display_network_stats()
        except Exception as e:
            self.fail(f"display_network_stats raised an exception: {e}")


def run_all_tests():
    """Run all tests and provide clear pass/fail results"""
    print("🔬 Running Automated Friendship Analyzer Tests...")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestFriendshipAnalyzer)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success Rate: {((result.testsRun - len(result.failures) - len(result.errors))/result.testsRun)*100:.1f}%")
    
    if result.wasSuccessful():
        print("\n🎉 ALL TESTS PASSED! ✅")
        print("The Friendship Analyzer is working correctly.")
        return True
    else:
        print(f"\n🚨 {len(result.failures) + len(result.errors)} TESTS FAILED! ❌")
        print("\nFailure/Error Details:")
        for test, error in result.failures + result.errors:
            print(f"❌ {test}")
            print(f"   {error.strip()}")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    print("\n" + "=" * 60)
    if success:
        print("🟢 SYSTEM STATUS: READY FOR DEPLOYMENT")
    else:
        print("🔴 SYSTEM STATUS: NEEDS ATTENTION")
    print("=" * 60)
    
    # Exit with appropriate code for CI/CD systems
    import sys
    sys.exit(0 if success else 1)
