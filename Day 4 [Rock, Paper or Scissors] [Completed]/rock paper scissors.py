import random

print('Welcome to the Rock Paper Scissors Game!!')

input_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices_list = [rock, paper, scissors]
random = random.randint(0, len(choices_list) - 1)
random_choice = choices_list[random]

if input_choice >= 3:
    print('Please try again you entered an invalid number!')
else:
    input_choice_figure = choices_list[input_choice]
    if input_choice == random:
        print('You chose:\n' + input_choice_figure + '\n' 'computer choose:\n' + random_choice + '\n' "It's Draw!")
    elif input_choice == 0:
        if random == 1:
            print('You chose:\n' + input_choice_figure + '\n' 'computer choose:\n' + random_choice + '\n''You Loose!')
        else:
            print('You chose:\n' + input_choice_figure + '\n' 'computer choose:\n' + random_choice + '\n''You Win!')
    elif input_choice == 1:
        if random == 0:
            print('You chose:\n' + input_choice_figure + '\n' 'computer choose:\n' + random_choice + '\n''You Win!')
        else:
            print('You chose:\n' + input_choice_figure + '\n' 'computer choose:\n' + random_choice + '\n''You Loose!')
    elif input_choice == 2:
        if random == 0:
            print('You chose:\n' + input_choice_figure + '\n' 'computer choose:\n' + random_choice + '\n''You Loose!')
        else:
            print('You chose:\n' + input_choice_figure + '\n' 'computer choose:\n' + random_choice + '\n' 'You Win!')
    else:
        print('Invalid input, please choose from 0, 1, 2')
