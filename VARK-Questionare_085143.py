class VARK:
    def __init__(self):
        self.questions = {
            1: {"question": "You are helping someone who wants to go to your airport, town centre or railway station. You would:",
                'choices': {'a': "go with her", 'b': "tell her the directions", 'c': "write down the directions", 'd': "draw or give a map"}},
            2: {"question": "You are not sure whether a word should be spelled 'dependent' or 'dependant'. You would:",
                'choices': {'a': "see the word in your mind", 'b': "sound it out", 'c': "look it up in the dictionary", 'd': "write both versions down and choose one"}},
            3: {"question": "You are planning a holiday for a group. You want some feedback from them about the plan. You would:",
                'choices': {'a': "use a map", 'b': "talk about it on the phone", 'c': "send them a copy of the printed itinerary", 'd': "describe some of the highlights"}},
            4: {"question": "You are going to cook something as a special treat. You would:",
                'choices': {'a': "cook something you know without needing instructions", 'b': "ask friends for suggestions", 'c': "look through the cookbook for ideas", 'd': "look at a few pictures in the cookbook"}},
            5: {"question": "A group of tourists want to learn about the parks or wildlife reserves in your area. You would:",
                'choices': {'a': "talk about the wildlife and forests", 'b': "show them maps and internet pictures", 'c': "take them to a park or reserve", 'd': "give them brochures and booklets"}},
            6: {"question": "You are learning to take photos with your new digital camera or mobile phone. You would:",
                'choices': {'a': "follow the instructions given in the manual", 'b': "talk to someone who knows about it", 'c': "use the controls and learn by trial and error", 'd': "see pictures showing how it is done"}},
            7: {"question": "You want to learn a new program, skill or game on a computer. You would:",
                'choices': {'a': "read the written instructions that came with the program", 'b': "talk with people who know about the program", 'c': "start using it and learn by trial and error", 'd': "follow diagrams in the manual"}},
            8: {"question": "You are choosing food at a restaurant or cafe. You would:",
                'choices': {'a': "choose something that you have had there before", 'b': "listen to the waiter or ask friends what they recommend", 'c': "choose from the descriptions in the menu", 'd': "look at pictures of each dish"}},
            9: {"question": "You have a problem with your heart. You would prefer that the doctor:",
                'choices': {'a': "show you a diagram of what was wrong", 'b': "describe what was wrong", 'c': "give you a pamphlet that explained the problem", 'd': "use a plastic model to show what was wrong"}},
            10: {"question": "You want to learn how to take better photos. You would:",
                'choices': {'a': "look at examples of good and poor photos", 'b': "read about the techniques from books", 'c': "ask questions and talk about the technique with others", 'd': "experiment with the camera and learn from trial and error"}},
            11: {"question": "You want to learn how to do something new on a computer. You would:",
                'choices': {'a': "read the manual", 'b': "ask someone who knows", 'c': "follow diagrams or pictures", 'd': "just try it and learn from mistakes"}},
            12: {"question": "You want to find out about a house or apartment. You would:",
                'choices': {'a': "read the description", 'b': "talk to the owner", 'c': "view a plan or map of the place", 'd': "look at pictures"}},
            13: {"question": "You are about to purchase a new digital camera or mobile phone. Other than price, what would most influence your decision?",
                'choices': {'a': "trying or testing it", 'b': "reading the details about its features", 'c': "it is a modern design and looks good", 'd': "the salesperson telling me about it"}},
            14: {"question": "You want some feedback about an event, competition or test. You would like to have feedback:",
                'choices': {'a': "using graphs showing what you achieved", 'b': "from somebody who talks it through with you", 'c': "using a written description of your results", 'd': "using examples from what you did"}},
            15: {"question": "You want to learn about a new issue or topic. You want to:",
                'choices': {'a': "read written reports, articles or books", 'b': "have diagrams or charts", 'c': "discuss it with others", 'd': "use hands-on experience"}},
            16: {"question": "You want to learn how to assemble a flat-pack piece of furniture. You would:",
                'choices': {'a': "follow the diagrams in the instructions", 'b': "read the instructions", 'c': "ask someone who has done it before", 'd': "follow your instincts and figure it out as you go"}}
        }
        self.scoring_chart = {
            1: {'a': 'K', 'b': 'A', 'c': 'R', 'd': 'V'},
            2: {'a': 'V', 'b': 'A', 'c': 'R', 'd': 'K'},
            3: {'a': 'V', 'b': 'A', 'c': 'R', 'd': 'K'},
            4: {'a': 'K', 'b': 'A', 'c': 'R', 'd': 'V'},
            5: {'a': 'A', 'b': 'V', 'c': 'K', 'd': 'R'},
            6: {'a': 'R', 'b': 'A', 'c': 'K', 'd': 'V'},
            7: {'a': 'R', 'b': 'A', 'c': 'K', 'd': 'V'},
            8: {'a': 'K', 'b': 'A', 'c': 'R', 'd': 'V'},
            9: {'a': 'V', 'b': 'A', 'c': 'R', 'd': 'K'},
            10: {'a': 'V', 'b': 'R', 'c': 'A', 'd': 'K'},
            11: {'a': 'R', 'b': 'A', 'c': 'V', 'd': 'K'},
            12: {'a': 'R', 'b': 'A', 'c': 'V', 'd': 'K'},
            13: {'a': 'K', 'b': 'R', 'c': 'V', 'd': 'A'},
            14: {'a': 'V', 'b': 'A', 'c': 'R', 'd': 'K'},
            15: {'a': 'R', 'b': 'V', 'c': 'A', 'd': 'K'},
            16: {'a': 'V', 'b': 'R', 'c': 'A', 'd': 'K'}
        }
        self.scores = {'V': 0, 'A': 0, 'R': 0, 'K': 0}

    def ask_questions(self):
        print("Please answer each question by entering 1 or 2 letters (e.g., 'a' or 'ab'):\n")
        for question_no, question_data in self.questions.items():
            print(f"\nQuestion {question_no}: {question_data['question']}")
            for option, description in question_data['choices'].items():
                print(f" {option}. {description}")
            while True:
                try:
                    user_input = input("Enter your choice: ").lower()
                    if len(user_input) < 1 or len(user_input) > 2:
                        raise ValueError("Enter 1 or 2 choices without spaces.")
                    if not all(character in question_data['choices'].keys() for character in user_input):
                        raise ValueError("Invalid choice entered. Please choose valid options.")
                    for character in user_input:
                        vark_type = self.scoring_chart[question_no][character]
                        self.scores[vark_type] += 1
                    break
                except ValueError as ve:
                    print(f"Error: {ve}")

    def show_result(self):
        print("\nYour VARK scores:")
        for style, score in self.scores.items():
            print(f"{style}: {score}")
        highest = max(self.scores, key=self.scores.get)
        print(f"\nYour dominant learning style is likely: {highest}")

if __name__ == "__main__":
    vark_quiz = VARK()
    vark_quiz.ask_questions()
    vark_quiz.show_result()