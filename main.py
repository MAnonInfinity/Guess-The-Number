import random
import art

def checkGuess(guess, number):
    """Checks whether the guess was correct"""
    if guess == number:
        print("You got it! You Win")
        return 1
    elif guess > number:
        print("Too high.")
        return -1
    else:
        print("Too low.")
        return -1

def guessTheNumber(attempts):
    """Driver code for the program"""
    print("Welcome to the Number Guessing Game!")
    print("\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        attempts = 10

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        userGuess = int(input("Make a guess: "))
        if checkGuess(userGuess, number) == -1:
            attempts -= 1
            if attempts == 0:
                print("You've ran out of guesses. You Lose.")
                break
            print("Guess again.")
        else:
            break
            
    print(f"The number is {number}.")

print(art.logo)
number = random.randint(1,100)
attempts = 5
guessTheNumber(attempts)

