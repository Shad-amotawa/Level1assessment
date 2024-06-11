import random


# Function to check yes/no responses
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please input a validated answer ")


# Functions for instructions
def instruction():
    print('''
   *** Instructions ***
   To begin, decide what kind of multiplication you would like (e.g., choose
   a number from one to twelve times table).

   Once you finish your quiz, your score will be calculated.
   ''')


# Function to ask questions
def question(num_questions):
    score = 0
    user_answers = []
    for _ in range(num_questions):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        while True:
            try:
                user_answer = int(input(f"What is {num1} times {num2}? "))
                break
            except ValueError:
                print("Please enter a number ")
        correct_answer = num1 * num2
        user_answers.append((f"What is {num1} times {num2}?", user_answer, correct_answer))
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
    print(f"Your score is {score} out of {num_questions}, which is {score / num_questions * 100:.2f}%.")
    return score, user_answers


# Function to show statistics
def statistics():
    pass


# Main program
total_games_played = 0
total_score = 0
all_questions_answers = []

while True:
    want_instructions = yes_no("Do you want to read the instructions? ")
    if want_instructions == "yes":
        instruction()
    print(f"You chose {want_instructions}")

    while True:
        try:
            num_questions = int(input("How many questions do you want to be asked? "))
            if num_questions <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer.")

    current_score, user_answers = question(num_questions)
    total_games_played += 1
    total_score += current_score
    all_questions_answers.extend(user_answers)

    play_again = yes_no("Do you want to take this quiz again? ")
# Quiz statistics
    if play_again == "no":
        print("\nQuiz Statistics:")
        print(f"Total Games Played: {total_games_played}")
        print(f"Total Score: {total_score}")
        print(f"Average Score: {total_score / total_games_played * 100 if total_games_played > 0 else 0:.2f}%")

        want_statistics = yes_no("Would you like to see the Quiz's history? ")
        if want_statistics == "yes":
            statistics()
        else:
            print("You choose no")
            break

        print(f"You chose {want_statistics}")
        print("Here are your questions and answers: ")
        for question, user_answer, correct_answer in all_questions_answers:
            print(f"Question: {question}")
            print(f"Your Answer: {user_answer}")
            print(f"Correct Answer: {correct_answer}")
        print("Thanks for taking this quiz!")
        break
