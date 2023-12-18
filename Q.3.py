import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Number of attempts allowed
    max_attempts = 5

    print("Welcome to the Guessing Game! Try to guess the number between 1 and 100.")

    for attempt in range(1, max_attempts + 1):
        try:
            # Get user input for the guess
            guess = int(input(f"Attempt {attempt}/{max_attempts}: Enter your guess: "))

            # Provide feedback based on the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the number.")
                return

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # If the loop completes without a correct guess
    print(f"Game over! You ran out of {max_attempts} guesses. The correct number was {secret_number}.")

# Run the guessing game
guessing_game()
