student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass


data = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = pandas.DataFrame(data)

phonetic = {row.letter:row.code for (index, row) in phonetic_dict.iterrows()}

word_input = input('Type a word: ').upper()

def generate_phonetic():
    try:
        phonetic_word = [phonetic[item] for item in word_input]
    except KeyError:
        print('Sorry only letters in the alphabet please.')
        generate_phonetic()
    else:
        print(phonetic_word)

generate_phonetic()