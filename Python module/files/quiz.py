def new_game():
    guesses = []
    correct_answers = []
    question_num = 0

    for key in questions:
        print("--------------------------------")
        print(key)
        for i in choices[question_num]:
            print(i)
        guess = input("Enter (A, B, C, D):").upper()

        # Validate input
        while guess not in ["A", "B", "C", "D"]:
            print("Invalid choice. Please enter A, B, C, or D.")
            guess = input("Enter (A, B, C, D):").upper()

        guesses.append(guess)
        correct_answers.append(check_answer(questions.get(key), guess))
        question_num += 1

    display_score(correct_answers, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct answer")
        return 1
    else:
        print("Wrong answer")
        return 0

def display_score(correct_answers, guesses):
    print("RESULTS")
    print("-------------------")
    print("Answers:", end=" ")
    for i in questions.values():
        print(i, end=" ")
    print()

    print("Guesses:", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((sum(correct_answers) / len(questions)) * 100)
    print("Your score is:", str(score) + "%")

def play_again():
    response = input("Do you want to play again? (y/n):").upper()
    return response == "Y"

questions = {
    "Who created earth?": "B",
    "Which date did Kenya gain Independence?": "C",
    "Who discovered the force of Gravity?": "B",
    "Who created Facebook?": "A"
}

choices = [
    ["A. Sciences", "B. God the Heavenly Father", "C. None of the Above", "D. No Idea"],
    ["A. 1st June 1963", "B. 20th October 1964", "C. 12th December 1963", "D. 12th December 1964"],
    ["A. John Bethwel", "B. Isaac Newton", "C. George Bool", "D. John Deere"],
    ["A. Mark Zuckerberg", "B. John Zuckerberg", "C. Bill Gates", "D. Elon Musk"]
]

new_game()

while play_again():
    new_game()

print("Byeeeeeeeeee")
