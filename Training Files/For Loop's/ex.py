line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# making the input into a list so separate the entries
rows = int(list(position)[1])
columns = list(position)[0]

# creating a loop to change the letters to numbers
if columns == 'A':
    columns = 1
elif columns == 'B':
    columns = 2
elif columns == 'C':
    columns = 3

# putting the entries into the list position indexes to replace the spot with X
map[rows - 1][columns - 1] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
