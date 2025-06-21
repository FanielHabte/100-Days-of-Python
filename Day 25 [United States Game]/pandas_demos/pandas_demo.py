import pandas as pd

data = pd.read_csv("weather_data.csv")

monday_temp = data.temp[data.day == "Monday"][0]


def convert_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


print(convert_to_fahrenheit(monday_temp))
#
# # create dataframe
#
# data_dict = {
#     "students": ["Amy", "Fani"],
#     "scores": [76, 56]
# }
#
# data = pd.DataFrame(data_dict)
#
# data.to_csv("new_data.csv")


# squirrel

# TODO: create a csv table that hold two column the color(Primary Fur Color) and count of squirrel

import pandas as pd

# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241229.csv", usecols=["Primary Fur Color", "Unique Squirrel ID"])
#
# aggregation = data.groupby("Primary Fur Color").count()
# renamed_data = pd.DataFrame(aggregation).rename(columns={"Unique Squirrel ID": "Count of Squirrel"})
#
# renamed_data.to_csv("count of squirrel.csv")


data = {
    "fani":["asmara","addis abeba","seattle"],
    "lemlem":["fano","fdaf","fasf"]
}

data_frame = pd.DataFrame(data).rename(columns={"fani":"fanni", "lemlem":"hagos"})

print(data_frame)