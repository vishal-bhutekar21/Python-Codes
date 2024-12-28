import random as r

# Generate a random number between 1 and 10
target = r.randint(1, 10)

while True:
    # Prompt the user to enter a number
    userchoice = int(input("Enter Your Random Number (between 1 and 10): "))

    if userchoice == target:
        # If the guess is correct, congratulate the user and break the loop
        print(f"Congratulations!! You have guessed the correct number: {userchoice}")
        break
    # Exit the loop after a correct guess
    else:
        # If the guess is wrong, inform the user and continue the loop
        print(f"Sorry, your guessed number {userchoice} is wrong. The actual number was: {target}")
print("========Game Over=========")