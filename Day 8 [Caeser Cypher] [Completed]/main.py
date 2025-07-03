from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(plain_text, shift_amount):
    output_text = ''
    for letter in plain_text:
        index = plain_text.index(letter)
        if letter not in alphabet:
            output_text += plain_text[index]
        elif letter in alphabet:
            position = alphabet.index(letter)
            length_alphabet = len(alphabet)
            if direction == 'encode':
                new_position = position + shift_amount
                if new_position > length_alphabet:
                    new_position -= length_alphabet
                new_letter = alphabet[new_position]
                output_text += new_letter
            if direction == 'decode':
                new_position = position - shift_amount
                new_letter = alphabet[new_position]
                output_text += new_letter
    print(f"Your {direction}d text is {output_text}\n")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(plain_text=text, shift_amount=shift)

    rerun = input('Would you like to rerun then game (yes/no)\n').lower()
    if rerun == 'no':
        should_continue = False
        print('Good Bye')
