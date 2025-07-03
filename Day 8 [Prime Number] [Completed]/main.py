# # Write your code below this line 👇
# import math
#
#
# def paint_calc(height, width, cover):
#     value = math.ceil(((height * width) / cover))
#     print(f"You will need {value} paints")
#
# # Write your code above this line 👆
# # Define a function called paint_calc() so the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input('What is the height fo the wall\n'))  # Height of wall (m)
# test_w = int(input('What is the weight of the wall\n'))  # Width of wall (m)
# coverage = 5
#
# paint_calc(height=test_h, width=test_w, cover=coverage)


# Write your code below this line 👇
def prime_checker(number):
    m = pow(n, 2)
    value_checked = ''
    for numbers in range(2, m):
        if numbers % n:
            value_checked = "It's a prime number."
        else:
            value_checked = "It's not a prime number."
    print(value_checked)
# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)
