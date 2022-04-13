# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

dict_nato = {}
list_nato_name = []

data_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter[0]: row.code for (index, row) in data_alphabet.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    input_word = input("Enter your name: ").upper()
    try:
        list_nato_name = [nato_dict[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only letters from the alphabet, please.")
        generate_phonetic()
    else:
        print(list_nato_name)

generate_phonetic()

