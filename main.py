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
