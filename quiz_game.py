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
                    if choice == self.answer:
                        print("✅ Correct!\n")
                        return True
                    else:
                        print(f"❌ Wrong! Correct answer is: {self.options[self.answer - 1]}\n")
                        return False
                else:
                    print("Please choose a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")


class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        print("\n🎉 Welcome to the Python Quiz Game!")
        print("----------------------------------")
        self.score = 0
        for q in self.questions:
            if q.ask():
                self.score += 1
        print(f"🎯 Your final score: {self.score}/{len(self.questions)}")

    def play(self):
        while True:
            self.start()
            again = input("Do you want to play again? (yes/no): ").lower()
            if again != "yes":
                print("Thank you for playing! 👋")
                break


# List of 10 Python Questions
questions = [
    Question("What is the correct file extension for Python files?", [".py", ".python", ".pt", ".pyt"], 1),
    Question("Which keyword is used to define a function in Python?", ["function", "def", "fun", "define"], 2),
    Question("What data type is the result of: 3 + 2.5?", ["int", "float", "str", "bool"], 2),
    Question("Which loop is used to iterate over a sequence?", ["for", "while", "if", "switch"], 1),
    Question("How do you insert COMMENTS in Python code?", ["//comment", "#comment", "/*comment*/", "--comment"], 2),
    Question("Which operator is used for exponentiation (power) in Python?", ["^", "**", "exp()", "pow()"], 2),
    Question("What is the output of 'bool(0)' in Python?", ["True", "False", "None", "0"], 2),
    Question("Which keyword is used to handle exceptions in Python?", ["catch", "error", "except", "exception"], 3),
    Question("How do you start a Python list?", ["()", "{}", "[]", "<>"], 3),
    Question("What is the correct way to create a dictionary in Python?", ["[]", "()", "{}", "<>"], 3),
]

# Start Game
if __name__ == "__main__":
    game = QuizGame(questions)
    game.play()
