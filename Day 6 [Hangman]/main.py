import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# remaining lives
lives = 6

# Create blanks
display = []
for _ in range(word_length):
    display.append('_')

checker = False
while not checker:
    guess = input("Please guess a letter:").lower()
    # Check for you guessed letter
    if guess not in chosen_word or guess in display:
        lives -= 1
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(''.join(display))

    # Check if user has got all letters.
    checker = '_' not in display
    if checker is True:
        print('You win')
    elif lives == 0:
        print('You Lose')
    # Print the Figure
    print(stages[lives])
    