# quiz_game.py

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def ask(self):
        print("\n" + self.prompt)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")
        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if 1 <= choice <= 4:
                    return choice == self.answer
                else:
                    print("Please choose between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")


class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        print("\nWelcome to the Quiz Game!")
        print("---------------------------")
        for q in self.questions:
            if q.ask():
                print("Correct!\n")
                self.score += 1
            else:
                print("Wrong!\n")
        print(f"Quiz finished! Your final score: {self.score}/{len(self.questions)}")


# List of Questions
questions = [
    Question("What is the capital of Pakistan?", ["Lahore", "Islamabad", "Karachi", "Quetta"], 2),
    Question("2 + 2 = ?", ["3", "4", "5", "2"], 2),
    Question("Who is the founder of Pakistan?", ["Iqbal", "Sir Syed", "Jinnah", "Bhutto"], 3),
    Question("What is the color of sky?", ["Blue", "Green", "Yellow", "Red"], 1),
    Question("HTML stands for?", ["Hyper Text Markup Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language", "High Text Machine Language"], 1),
]

# Start Game
game = QuizGame(questions)
game.start()
git init