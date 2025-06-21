# # key = the name of the dictionaries
# # value = the meaning of the dictionaries
# # {key : value}
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# # print(programming_dictionary["Bug"])
#
# # it's a Key error then it's a typo
#
# # Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."
#
#
# # Creating an empty dictionary
# # empty_dictionary = {}
#
# # Wipe an existing dictionary
# # programming_dictionary = {}
#
# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A math in you computer"
# print(programming_dictionary)
#
# # Loop through a dictionary
# for key in programming_dictionary:
#     print(f"{key}: {programming_dictionary[key]}")

####################################

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list a dictionary

# traveling_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# Nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "date_visited": ['08/23/2023', '08/24/2023', '08/25/2023']},
    "Germany": {'cities_visited': ["Berlin", "Hamburg", "Stuttgart"], "date_visited": ['09/23/2023', '08/24/2023', '08/25/2023']},
}
print(travel_log)

list()
# Nesting a dictionary in a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "date_visited": ['08/23/2023', '08/24/2023', '08/25/2023']
     },
    {
        "country": 'Germany',
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "date_visited": ['09/23/2023', '08/24/2023', '08/25/2023']
     },
]
print(travel_log)