import random

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
# Generate secret number
myNumber = random.randint(smaller, larger)
count = 0
# Start game loop
while True:
    count += 1
    # User's guess
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small")
    elif userNumber > myNumber:
        print("Too large")
    else:
        print("You've got it in", count, "tries!")
        print("You win!")
        break
    # Computer's guess
    computerNumber = random.randint(smaller, larger)
    print(f"Computer's guess: {computerNumber}")
    if computerNumber < myNumber:
        print("Computer's guess is too small.")
    elif computerNumber > myNumber:
        print("Computer's guess is too large.")
    else:
        print("Computer guessed the correct number!")
        print("Computer wins!")
        break
