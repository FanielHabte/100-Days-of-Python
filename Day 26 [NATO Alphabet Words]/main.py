import pandas as pd
# TODO 1. Create a dictionary in this format:
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


nato_phonetic_csv = pd.read_csv(
    "Day 26 [NATO Alphabet Words]/nato_phonetic_alphabet.csv"
)
nato_phonetic = {row.letter.upper(): row.code for (index, row) in nato_phonetic_csv.iterrows()}

word = input('Please provide a word: ')
word_nato_phonetic = {letter.upper(): nato_phonetic[letter.upper()] for letter in word}
print(word_nato_phonetic)
