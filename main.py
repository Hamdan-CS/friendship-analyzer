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

class FriendshipAnalyzer:
    """AI system to analyze friendship compatibility"""
        def calculate_interest_compatibility(self, person1, person2):
        """Calculate compatibility based on shared interests"""
        shared_interests = set(person1.interests) & set(person2.interests)
        total_interests = set(person1.interests) | set(person2.interests)

        if len(total_interests) == 0:
            return 0

        similarity = len(shared_interests) / len(total_interests)
        return similarity * 10  # Scale to 0-10

    def calculate_age_compatibility(self, person1, person2):
        """Calculate compatibility based on age difference"""
        age_diff = abs(person1.age - person2.age)

        if age_diff <= 2:
            return 10
        elif age_diff <= 5:
            return 8
        elif age_diff <= 10:
            return 6
        elif age_diff <= 15:
            return 4
        else:
            return 2


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
        """Main function to analyze overall compatibility"""
        pass

    def provide_recommendation(self, person1, person2, overall_score, detailed_scores):
        """AI recommendation based on compatibility"""
        pass

    def find_best_matches(self, person):
        """Find best friendship matches for a person"""
        pass

    def create_friendship_network(self):
        """Create friendships between compatible people"""
        pass

    def display_network_stats(self):
        """Display statistics about the friendship network"""
        pass

