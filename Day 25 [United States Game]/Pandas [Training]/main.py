# import csv
import pandas as pd
# # TODO: open and read the csv file then add each line to a list
#
#
# with open("weather_data.csv") as csv_data:
#     reader = csv.reader(csv_data)
#     temperatures = []
#     for row in reader:
#         if row[1] != 'temp':
#             temperature = int(row[1])
#             temperatures.append(temperature)
#
#     print(temperatures)


data = pd.read_csv("weather_data.csv")
print(data)