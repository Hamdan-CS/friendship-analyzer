# AI-Powered Friendship Compatibility Analyzer

"""
This project analyzes friendship compatibility using Python and OOP.
We'll gradually build it up step-by-step.
"""
class Person:
    """Represents a person with their characteristics and preferences"""
    
    def __init__(self, name, age, interests, personality_traits, communication_style):
        self.name = name
        self.age = age
        self.interests = interests  # List of interests
        self.personality_traits = personality_traits  # Dictionary with scores 0-10
        self.communication_style = communication_style  # Dictionary with preferences
        self.friendships = []

    def display_info(self):
        """Display person's information in a formatted way"""
        print(f"\n{'='*50}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Interests: {', '.join(self.interests)}")
        print(f"Personality Traits:")
        for trait, score in self.personality_traits.items():
            print(f"  - {trait.title()}: {score}/10")
        print(f"Communication Style:")
        for style, score in self.communication_style.items():
            print(f"  - {style.title()}: {score}/10")
        print(f"{'='*50}")



    def __init__(self):
        self.people = []
        self.compatibility_threshold = 7.0  # Minimum score for good compatibility

    def add_person(self, person):
        """Add a person to the system"""
        pass

    def calculate_interest_compatibility(self, person1, person2):
        """Calculate compatibility based on shared interests"""
        pass

    def calculate_personality_compatibility(self, person1, person2):
        """Calculate compatibility based on personality traits"""
        pass

    def calculate_communication_compatibility(self, person1, person2):
        """Calculate compatibility based on communication styles"""
        pass

    def calculate_age_compatibility(self, person1, person2):
        """Calculate compatibility based on age difference"""
        pass

def analyze_compatibility(self, person1, person2):
    """Main AI function to analyze overall compatibility"""
    print(f"\n🤖 Analyzing compatibility between {person1.name} and {person2.name}...")

    interest_score = self.calculate_interest_compatibility(person1, person2)
    personality_score = self.calculate_personality_compatibility(person1, person2)
    communication_score = self.calculate_communication_compatibility(person1, person2)
    age_score = self.calculate_age_compatibility(person1, person2)

    weights = {
        'interests': 0.3,
        'personality': 0.4,
        'communication': 0.2,
        'age': 0.1
    }

    overall_score = (
        interest_score * weights['interests'] +
        personality_score * weights['personality'] +
        communication_score * weights['communication'] +
        age_score * weights['age']
    )

    print(f"\n📊 Compatibility Analysis Results:")
    print(f"{'─'*40}")
    print(f"Interest Compatibility: {interest_score:.1f}/10")
    print(f"Personality Compatibility: {personality_score:.1f}/10")
    print(f"Communication Compatibility: {communication_score:.1f}/10")
    print(f"Age Compatibility: {age_score:.1f}/10")
    print(f"{'─'*40}")
    print(f"Overall Compatibility: {overall_score:.1f}/10")

    self.provide_recommendation(person1, person2, overall_score, {
        'interests': interest_score,
        'personality': personality_score,
        'communication': communication_score,
        'age': age_score
    })

    return overall_score


def provide_recommendation(self, person1, person2, overall_score, detailed_scores):
    """AI-powered recommendation based on analysis"""
    print(f"\n🎯 AI Recommendation:")

    if overall_score >= 8.5:
        print("🌟 EXCELLENT MATCH! This friendship has amazing potential!")
    elif overall_score >= 7.0:
        print("✨ GREAT MATCH! This friendship looks very promising!")
    elif overall_score >= 5.5:
        print("👍 GOOD POTENTIAL! This friendship could work well with some effort.")
    elif overall_score >= 4.0:
        print("⚠️  MODERATE COMPATIBILITY. Friendship possible but may require work.")
    else:
        print("❌ LOW COMPATIBILITY. This friendship might be challenging.")

    print(f"\n💡 Specific Insights:")
    if detailed_scores['interests'] < 5:
        print("• Try exploring new activities together to find common interests")
    if detailed_scores['personality'] < 5:
        print("• Your personality differences could complement each other")
    if detailed_scores['communication'] < 5:
        print("• Work on understanding each other's communication styles")

    strongest_aspect = max(detailed_scores, key=detailed_scores.get)
    print(f"• Your strongest connection is in: {strongest_aspect}")


    def find_best_matches(self, person):
        """Find the best friendship matches for a person"""
        print(f"\n🔍 Finding best matches for {person.name}...")

        matches = []
        for other_person in self.people:
            if other_person != person:
                score = self.analyze_compatibility(person, other_person)
                matches.append((other_person, score))

        matches.sort(key=lambda x: x[1], reverse=True)

        print(f"\n🏆 Top Friendship Matches for {person.name}:")
        print("=" * 50)
        for i, (match, score) in enumerate(matches[:3], 1):
            print(f"{i}. {match.name} - Compatibility: {score:.1f}/10")

        return matches

    def create_friendship_network(self):
        """Create friendships between compatible people"""
        print(f"\n🌐 Creating Friendship Network...")

        for person in self.people:
            for other_person in self.people:
                if person != other_person:
                    score = self.analyze_compatibility(person, other_person)
                    if score >= self.compatibility_threshold:
                        person.friendships.append({
                            'friend': other_person,
                            'compatibility_score': score
                        })

        self.display_network_stats()


        def create_friendship_network(self):
        """Create friendships between compatible people"""
        print(f"\n🌐 Creating Friendship Network...")

        for person in self.people:
            for other_person in self.people:
                if person != other_person:
                    score = self.analyze_compatibility(person, other_person)
                    if score >= self.compatibility_threshold:
                        person.friendships.append({
                            'friend': other_person,
                            'compatibility_score': score
                        })

        self.display_network_stats()

    def display_network_stats(self):
        """Display statistics about the friendship network"""
        print(f"\n📈 Network Statistics:")
        print("=" * 30)

        total_friendships = sum(len(person.friendships) for person in self.people)
        avg_friendships = total_friendships / len(self.people) if self.people else 0

        print(f"Total People: {len(self.people)}")
        print(f"Total Friendships: {total_friendships}")
        print(f"Average Friendships per Person: {avg_friendships:.1f}")


def demo():
    """Demonstration of the AI Friendship Analyzer"""
    print("🤖 Welcome to AI-Powered Friendship Compatibility Analyzer!")
    print("=" * 60)

    analyzer = FriendshipAnalyzer()

    alice = Person(
        name="Alice",
        age=22,
        interests=["reading", "hiking", "photography", "cooking"],
        personality_traits={
            "extroversion": 7,
            "openness": 8,
            "agreeableness": 9,
            "conscientiousness": 8,
            "neuroticism": 3
        },
        communication_style={
            "direct": 6,
            "emotional": 7,
            "humor": 8,
            "formal": 4
        }
    )

    bob = Person(
        name="Bob",
        age=25,
        interests=["hiking", "gaming", "music", "travel"],
        personality_traits={
            "extroversion": 6,
            "openness": 9,
            "agreeableness": 7,
            "conscientiousness": 6,
            "neuroticism": 4
        },
        communication_style={
            "direct": 8,
            "emotional": 5,
            "humor": 9,
            "formal": 3
        }
    )

    carol = Person(
        name="Carol",
        age=20,
        interests=["reading", "art", "photography", "movies"],
        personality_traits={
            "extroversion": 8,
            "openness": 9,
            "agreeableness": 8,
            "conscientiousness": 7,
            "neuroticism": 2
        },
        communication_style={
            "direct": 5,
            "emotional": 8,
            "humor": 7,
            "formal": 5
        }
    )

    analyzer.add_person(alice)
    analyzer.add_person(bob)
    analyzer.add_person(carol)

    alice.display_info()
    bob.display_info()
    carol.display_info()

    analyzer.analyze_compatibility(alice, bob)
    analyzer.analyze_compatibility(alice, carol)
    analyzer.analyze_compatibility(bob, carol)

    analyzer.find_best_matches(alice)
    analyzer.create_friendship_network()


