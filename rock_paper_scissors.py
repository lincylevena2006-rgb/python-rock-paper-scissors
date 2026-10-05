import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("================================")
print("       ROCK PAPER SCISSORS")
print("================================")

while True:
    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "4":
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice!")
        continue

    user = choices[int(choice) - 1]
    computer = random.choice(choices)

    print("You:", user)
    print("Computer:", computer)

    if user == computer:
        print("It's a draw!")

    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Score:", user_score, "-", computer_score)

print("\nThanks for playing!")