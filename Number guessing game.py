import random
# ! When the game starts, it should display a welcome message along with the rules of the game.
# ! The computer should randomly select a number between 1 and 100.
# ! User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.
# ! The user should be able to enter their guess.
# ! If the user’s guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.
# ! If the user’s guess is incorrect, the game should display a message indicating whether the number is greater or less than the user’s guess.
# ! The game should end when the user guesses the correct number or runs out of chances.
chances = 0
computer_n = random.randint(1, 100)

print("Welcome to the number guessing game from 1 to 100!")
print("Select the difficulty:")
print("Easy (15 chances): 1 ")
print("Medium (10 chances): 2")
print("Hard (5 chances): 3")
difficulty = int(input("Enter the difficulyt as a number: "))

if difficulty == 1:
    print("You have entered easy mode")
    while chances <= 15:
        guess = int(input("Enter your guess: "))
        if guess == computer_n:
            print("Congratulations! You guessed the number! ")
            quit()
        elif guess > computer_n:
            print("The number is lower")
        else:
            print("The number is higher")
        chances += 1

if difficulty == 2:
    print("You have entered medium mode")
    while chances <= 10:
        guess = int(input("Enter your guess: "))
        if guess == computer_n:
            print("Congratulations! You guessed the number! ")
            quit()
        elif guess > computer_n:
            print("The number is lower")
        else:
            print("The number is higher")
        chances += 1

if difficulty == 3:
    print("You have entered difficult mode")
    while chances < 5:
        guess = int(input("Enter your guess: "))
        if guess == computer_n:
            print("Congratulations! You guessed the number! ")
            quit()
        elif guess > computer_n:
            print("The number is lower")
        else:
            print("The number is higher")
        chances += 1

print("The computer won! Your bad")
