import random

# Function to ask yes/no questions and makes sure there isn't any unexpexted code is being used
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes or no")

# Function to display instructions if the user wants them
def instruction():
    print('''
   *** Instructions ***
   To begin, decide what kind of multiplication you would like (e.g., choose
   a number from one to twelve times table).

   Once you finish your quiz, your score will be calculated.
   ''')

# Function to ask questions for the quiz
def question():
    score = 0
    user_answer = 0
    for _ in range(5):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        while True:
            try:
                user_answer = int(input(f"What is {num1} times {num2}? "))
                break
            except ValueError:
                print("Please enter a number ")
        correct_answer = num1 * num2
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
    print(f"Your score is {score} out of 5.")
    return score

# main routine
total_games_played = 0
total_score = 0

while True:
    want_instructions = yes_no("Do you want to read the instructions? ")
    if want_instructions == "yes":
        instruction()
    print(f"You chose {want_instructions}")
    current_score = question()
    total_games_played += 1
    total_score += current_score
# if the user wants to take the quiz again
    play_again = yes_no("Do you want to take this quiz again? ")

# Functions the amount of question the user gets right
    if play_again == "no":
        print("\nQuiz Statistics:")
        print(f"Total Games Played: {total_games_played}")
        print(f"Total Score: {total_score}")
        print(f"Average Score: {total_score / total_games_played if total_games_played > 0 else 0}")
        print("Thanks for taking this quiz!")
        break
