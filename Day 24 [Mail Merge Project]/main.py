# TODO: create a letter using starting_letter.txt
# Replace the [name] placeholder with the actual name
# Save the letters in the folder "ReadyToSend"

with open("Input/Names/invited_names.txt") as guests:
    invited_guests = guests.readlines()

with open("Input/Letters/starting_letter.txt") as template:
    letter_template = template.read()

for invited_guest in invited_guests:
    striped_names = invited_guest.strip()
    custom_letter = letter_template.replace("[name]", striped_names)
    with open(f"./Output/ReadyToSend/Letter_For_{striped_names}", mode="w") as custom_template:
        custom_template.write(custom_letter)
