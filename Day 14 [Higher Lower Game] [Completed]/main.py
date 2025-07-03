import random
from art import logo, vs
from game_data import data

print(logo)


def random_generator():
    length_list = len(data)
    first_random_number = random.randrange(0, length_list)
    second_random_number = random.randrange(0, length_list)
    if first_random_number == second_random_number:
        second_random_number = random.randrange(0, length_list)
    return first_random_number, second_random_number


def data_format():
    first_random_number, second_random_number = random_generator()
    first_choice = data[first_random_number]
    second_choice = data[second_random_number]
    first_name = first_choice['name']
    first_description = first_choice['description']
    first_country = first_choice['country']
    a = first_choice['follower_count']
    second_name = second_choice['name']
    second_description = second_choice['description']
    second_country = second_choice['country']
    b = second_choice['follower_count']
    print(f"A: {first_name} a {first_description}, from {first_country}")
    print(vs)
    print(f"B: {second_name} a {second_description} from {second_country}")
    return a, b


user_is_right = True
score = 0
while user_is_right:
    if score > 0:
        print(f"You are right! Current score: {score}")

    random_generator()
    a, b = data_format()
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == 'a':
        if a > b:
            score += 1
        else:
            user_is_right = False
            print(f"Sorry, that's wrong. final score: {score}")
    elif user_choice == 'b':
        if b > a:
            score += 1
        else:
            user_is_right = False
            print(f"Sorry, that's wrong. final score: {score}")
