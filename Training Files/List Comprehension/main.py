"""
Increment all number in the list by one.
 Key work method.
   List Comprehension Syntax:
       new_list =  [item * 1 for item in old_list]"""

numbers = [1, 2, 3, 4]
new_numbers = [item + 1 for item in numbers]

"""
Challenge 1.
Create a range 1 to 5 and double each number using list comprehension
"""

doubled_numbers = [num * 2 for num in range(1, 5)]

# print(doubled_numbers)

"""
Challenge 2.
Create a list with all alphabetical words and order the list in asc using pangram
E.g pangram -> The quick brown fox jumps over the lazy dog
isalpha() removes non words, {} creates set removing duplicates, sorted always returns lists """

pangram = "The quick brown fox jumps over the lazy dog"
alphabet_list = sorted({word.upper() for word in pangram.lower() if word.isalpha()})

# print(alphabet_list)

"""
Challenge 3.
Get the intersecting number between the files"""

file1 = open("Training Files/List Comprehension/new1.txt", "r")
file2 = open("Training Files/List Comprehension/new2.txt", "r")

file1_num = [int(num.strip("\n")) for num in file1.readlines()]
file2_num = [int(num.strip("\n")) for num in file2.readlines()]

result = sorted({value for value in file1_num if value in file2_num})

# print(result)

"""
Challenge 4.
Assign random test scores for each student and put the values in a dictionary"""
import random

student = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanore', 'Freddie']
student_test_scores = {student: random.randint(1,100) for student in student}

passed_students = {
    students: scores
    for (students, scores) in student_test_scores.items()
    if scores > 50
}

"""
Challenge 5.
You are going to use Dictionary Comprehension to create a dictionary called result
that takes each word in the given sentence and calculates the number of letters in each word.   
"""
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_length = {value: len(value) for value in sentence.split()}

# print(words_length)

"""
Challenge 6.
You are going to use Dictionary Comprehension to create a dictionary called weather_f 
that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit. 

To convert temp_c into temp_f use this formula: 
(temp_c * 9/5) + 32 = temp_f
"""
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {key: (value * 9/5) + 32 for (key,value) in weather_c.items()}

# print(weather_f)

"""
Challenge 7.
Pandas iterrows to loop through the rows of a pandas dataframe
"""
import pandas as pd 

students = {
    'student' : ['Alex', 'Lily', 'John']
    , 'score' : [20, 40, 60]
}

students_df = pd.DataFrame(students)

for (index, row) in students_df.iterrows():
    if row.student == "Alex":
        print(row.score)

# print(students_df)
