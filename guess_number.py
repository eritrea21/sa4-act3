import random 

def guess_number():
    number = random.randint(1, 100)
    while True:
        guess = input("Guess a number between 1 and 100, or 'q' to quite: ")
        if guess.lower()== 'q':
            print(f"The number was {number}.")
            break
        try:
            guess = int(guess)
            if guess == number:
                print("Congratulation! You guessed the correct number.")
                break
            else:
                print("Incorrect guess. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")

