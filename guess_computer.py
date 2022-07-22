import random

maximum_value = int(input("Maximum Value: "))

def guess(maximum_value):
    random_number = random.randint(1, maximum_value)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {maximum_value}: "))
        if guess < random_number:
            guess = print("Incorrect. Too low. Try again")
        elif guess > random_number:
            guess = print("Incorrect. Too high. Try again")

    print("Congratulations! You have guessed the number.")

if __name__ == "__main__":
    guess(maximum_value)