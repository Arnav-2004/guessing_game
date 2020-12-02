import random

class NonIntegerError(ValueError):
    pass

print("Guessing game!\n")

def game():
    secret_num = random.randint(1, 20)
    guess_count = 1
    while True:
        guess = input("Please guess a number from 1 to 20: ")
        try:
            guess = int(guess)
        except ValueError:
            raise NonIntegerError(guess) from None

        if guess == secret_num:
            print(f"Congratulations, you guessed the correct number in {guess_count} chance(s)!\n")
            response = input("Do you want to play again? (Y/n): ")
            if response.lower() == 'n':
                print("\nThanks for playing, Have a great day!")
                break
            else:
                guess_count = 1
                secret_num = random.randint(1, 20)
                continue
        elif guess > secret_num:
            print(f"The number is smaller than {guess}!\n")
            guess_count += 1
        else:
            print(f"The number is greater than {guess}!\n")
            guess_count +=1
game()