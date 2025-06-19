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
        self.interests = interests
        self.personality_traits = personality_traits
        self.communication_style = communication_style
        self.friendships = []

    def display_info(self):
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

    def compatibility_strategy(self, other):
        return 5

class EmpatheticPerson(Person):
    def compatibility_strategy(self, other):
        return 10 if "emotional" in other.communication_style else 4

class LogicalPerson(Person):
    def compatibility_strategy(self, other):
        return 10 if "direct" in other.communication_style else 3

class CreativePerson(Person):
    def compatibility_strategy(self, other):
        return 10 if "humor" in other.communication_style or "openness" in other.personality_traits else 5

class ReservedPerson(Person):
    def compatibility_strategy(self, other):
        return 9 if other.personality_traits.get("extroversion", 0) <= 4 else 4

class EnergeticPerson(Person):
    def compatibility_strategy(self, other):
        return 10 if other.personality_traits.get("extroversion", 0) >= 7 else 5

class AnalyticalPerson(Person):
    def compatibility_strategy(self, other):
        diff = abs(self.personality_traits.get("conscientiousness", 5) - other.personality_traits.get("conscientiousness", 5))
        return 10 - diff

class AdventurousPerson(Person):
    def compatibility_strategy(self, other):
        return 10 if other.personality_traits.get("openness", 0) >= 7 else 5

class IntrovertPerson(Person):
    def compatibility_strategy(self, other):
        return 10 if other.personality_traits.get("extroversion", 0) <= 4 else 3

class HumorousPerson(Person):
    def compatibility_strategy(self, other):
        return 10 if other.communication_style.get("humor", 0) >= 7 else 5

class FriendshipAnalyzer:
    def __init__(self):
        self.people = []
        self.compatibility_threshold = 7.0

    def add_person(self, person):
        self.people.append(person)

    def calculate_interest_compatibility(self, person1, person2):
        shared_interests = set(person1.interests) & set(person2.interests)
        total_interests = set(person1.interests) | set(person2.interests)
        if not total_interests:
            return 0
        return (len(shared_interests) / len(total_interests)) * 10

    def calculate_personality_compatibility(self, person1, person2):
        score = 0
        traits = person1.personality_traits.keys()
        for trait in traits:
            score += 10 - abs(person1.personality_traits[trait] - person2.personality_traits[trait])
        return score / len(traits)

    def calculate_communication_compatibility(self, person1, person2):
        score = 0
        styles = person1.communication_style.keys()
        for style in styles:
            score += 10 - abs(person1.communication_style[style] - person2.communication_style[style])
        return score / len(styles)

    def calculate_age_compatibility(self, person1, person2):
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

    def analyze_compatibility(self, person1, person2):
        print(f"\n🤖 Analyzing compatibility between {person1.name} and {person2.name}...")

        interest_score = self.calculate_interest_compatibility(person1, person2)
        personality_score = self.calculate_personality_compatibility(person1, person2)
        communication_score = self.calculate_communication_compatibility(person1, person2)
        age_score = self.calculate_age_compatibility(person1, person2)
        strategy_score = person1.compatibility_strategy(person2)

        weights = {
            'interests': 0.3,
            'personality': 0.3,
            'communication': 0.2,
            'age': 0.1,
            'strategy': 0.1
        }

        overall_score = (
            interest_score * weights['interests'] +
            personality_score * weights['personality'] +
            communication_score * weights['communication'] +
            age_score * weights['age'] +
            strategy_score * weights['strategy']
        )

        print(f"\n📊 Compatibility Analysis Results:")
        print(f"{'─'*40}")
        print(f"Interest Compatibility: {interest_score:.1f}/10")
        print(f"Personality Compatibility: {personality_score:.1f}/10")
        print(f"Communication Compatibility: {communication_score:.1f}/10")
        print(f"Age Compatibility: {age_score:.1f}/10")
        print(f"Strategy Compatibility: {strategy_score:.1f}/10")
        print(f"{'─'*40}")
        print(f"Overall Compatibility: {overall_score:.1f}/10")

        self.provide_recommendation(person1, person2, overall_score, {
            'interests': interest_score,
            'personality': personality_score,
            'communication': communication_score,
            'age': age_score,
            'strategy': strategy_score
        })

        return overall_score

    def provide_recommendation(self, person1, person2, overall_score, detailed_scores):
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
        for key, score in detailed_scores.items():
            if score < 5:
                print(f"• {key.title()} could be improved for better compatibility.")

        strongest_aspect = max(detailed_scores, key=detailed_scores.get)
        print(f"• Your strongest connection is in: {strongest_aspect}")

    def find_best_matches(self, person):
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
        print(f"\n📈 Network Statistics:")
        print("=" * 30)
        total_friendships = sum(len(person.friendships) for person in self.people)
        avg_friendships = total_friendships / len(self.people) if self.people else 0
        print(f"Total People: {len(self.people)}")
        print(f"Total Friendships: {total_friendships}")
        print(f"Average Friendships per Person: {avg_friendships:.1f}")

def create_person():
    print("\n🧑 Enter New Person Details")
    name = input("Name: ")
    age = int(input("Age: "))
    interests = input("Interests (comma separated): ").split(',')
    interests = [i.strip() for i in interests]
    print("Enter Personality Traits (0-10):")
    traits = ['extroversion', 'openness', 'agreeableness', 'conscientiousness', 'neuroticism']
    personality_traits = {t: int(input(f"  {t.title()}: ")) for t in traits}
    print("Enter Communication Styles (0-10):")
    styles = ['direct', 'emotional', 'humor', 'formal']
    communication_style = {s: int(input(f"  {s.title()}: ")) for s in styles}

    return Person(name, age, interests, personality_traits, communication_style)

def demo():
    print("🤖 Welcome to AI-Powered Friendship Compatibility Analyzer!")
    print("=" * 60)

    analyzer = FriendshipAnalyzer()

    while True:
        add_more = input("\nWould you like to add a person? (yes/no): ").strip().lower()
        if add_more == 'yes':
            person = create_person()
            analyzer.add_person(person)
        else:
            break

    for person in analyzer.people:
        person.display_info()

    if len(analyzer.people) >= 2:
        analyzer.analyze_compatibility(analyzer.people[0], analyzer.people[1])
        analyzer.find_best_matches(analyzer.people[0])
        analyzer.create_friendship_network()
    else:
        print("\nNot enough people to analyze compatibility.")

if __name__ == "__main__":
    demo()
