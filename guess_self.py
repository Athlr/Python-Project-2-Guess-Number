import random

maximum_value = int(input("Maximum Value: "))

def guess(maximum_value):
    min = 1
    max = maximum_value
    user_response = " "

    while user_response != "c":
        if min != max:
            computer_guess_value = random.randint(min, max)
        else: 
            computer_guess_value = min

        user_response = input(f"Is the number in your head {computer_guess_value}? Enter correct(c), too high(h), or too low(l): ").lower()

        if user_response == "h":
            max = computer_guess_value - 1
        elif user_response == "l":
            min = computer_guess_value + 1

    print(f"Yay! We have correctly guess {user_response}, the number in your head!")

if __name__ == "__main__":
    guess(maximum_value)

        
