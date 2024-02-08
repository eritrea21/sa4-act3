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
            elif guess < number:
                print("Too low. Try again.")
<<<<<<< HEAD
            else:
                print("Too high. Try again.")
            guess_left -= 1
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
    
    if guess_left == 0:
        print(f"Sorry, you've run out of guesses. The number was {number}")
=======
                
            else:
                print("To high. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
>>>>>>> guess-hints
guess_number()

