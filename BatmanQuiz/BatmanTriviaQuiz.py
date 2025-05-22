import random
import datetime

# Ask the user a question
def askQuestion(question, options, correctAnswer):
    print(question)
    print(options)
    userAnswer = input("Enter your answer here: ")
    if userAnswer.upper() == correctAnswer.upper():
        return True
    else:
        return False

# Run the quiz
def quiz(questions):
    userScore = 0
    random.shuffle(questions)
    usersName = input("Enter your name: ")

    while True:
        timeStarted = datetime.datetime.now()
        print("Time Started: ", timeStarted.strftime("%Y-%m-%d %H:%M:%S"))

        for q in questions:
            is_correct = askQuestion(q["question"], q["options"], q["answer"])
            if is_correct:
                userScore += 1
                print("Correct!")
            else:
                print("Oops! The right answer was...")
                print(q["answer"])

        print("\nQuiz Complete")
        print("Your final Score:", userScore, "/", len(questions))

        if userScore <= 2:
            print("The Joker must've deceived you.")
        elif userScore <= 4:
            print("Nice Job, You're an ally of Gotham City!")
        else:
            print("Are you Bruce Wayne?! Legendary Job!")

        repeat = input("Would you like to do the Quiz Again? (Y/N): ")
        if repeat.upper() == "Y":
            userScore = 0  # Reset score for next round
            continue
        else:
            break

    # Save score to file
    with open("batman_quizscores.txt", "a") as resultFile:
        resultFile.write(f"{usersName} scored {userScore}/{len(questions)} on {timeStarted.strftime('%Y-%m-%d %H:%M:%S')}\n")

# View leaderboard
def leaderboard(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.readlines()
            print("\n--- Leaderboard ---")
            for line in content:
                print(line.strip())
            print("-------------------\n")
    except FileNotFoundError:
        print("No leaderboard data found yet.")

# Main menu
def mainMenu():
    while True: 
        print("WELCOME TO THE BATMAN TRIVIA QUIZ")
        print("----------------------------------")
        print("1. START THE BATMAN QUIZ - TYPE (START)")
        print("2. VIEW THE LEADERBOARDS - TYPE (VIEW)")
        print("3. EXIT - TYPE (EXIT)")
        print("----------------------------------")

        user_decision = input("Enter your choice here: ")
        if user_decision.upper() == "START":
            quiz(batcave)
        elif user_decision.upper() == "VIEW":
            leaderboard("batman_quizscores.txt")
        elif user_decision.upper() == "EXIT":
            print("Goodbye, Gotham defender!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# List of quiz questions
batcave = [
    {
        "question": "What is the highest Earning Batman Movie at the Box Office?", 
        "options": "A) Batman 1989  B) Batman Begins  C) The Batman  D) The Dark Knight",
        "answer": "D"
    },
    {
        "question": "What Year was Batman Created?",
        "options": "A) 1966  B) 1939  C) 1938  D) 1947",
        "answer": "B"
    },
    {
        "question": "Which actor is famous for portraying Robin in the 1966 television series?",
        "options": "A) Chris O'Donnell  B) Burt Ward  C) Scott Menville  D) Brenton Thwaites", 
        "answer": "B"
    },
    {
        "question": "Where does Bruce Wayne reside?",
        "options": "A) Wayne Manor  B) Smallville  C) Krypton  D) New York City", 
        "answer": "A"
    },
    {
        "question": "Who won an Oscar for their portrayal of a famous Batman supervillain?",
        "options": "A) Paul Dano  B) Jim Carrey  C) Jack Nicholson  D) Heath Ledger", 
        "answer": "D"
    }
]

# Start the program
if __name__ == "__main__":
    mainMenu()
