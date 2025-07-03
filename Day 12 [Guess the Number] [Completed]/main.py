import random
from art import logo

print(logo)


def number_of_tries():
    difficulty = input("Choose a Difficulty type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return 10
    else:
        return 5


def check_answer(guess, answer, turns):
    if guess == answer:
        print(f"You are right the number was {guess}!")
    elif guess > answer:
        print('Too High')
        return turns - 1
    else:
        print('Too Low')
        return turns - 1


def game():
    print("Welcome to the number guessing game")
    print("I\'m thinking of a number between 1 to 100")

    # generate a random number
    random_number = random.randint(1, 100)
    print(f"psst the correct numbers is {random_number}")

    turns = number_of_tries()
    guessed_number = 0
    while guessed_number != random_number:
        print(f"You have {turns} attempts remaining to guess the number")
        guessed_number = int(input("Make a guess: "))
        turns = check_answer(guessed_number, random_number, turns)

        if turns == 0:
            print("You lose!, you have run out of turns")
            return


game()
