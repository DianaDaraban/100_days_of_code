#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Letters/starting_letter.txt', 'r') as f:
    starting_letter = f.readlines()

with open('./Input/Names/invited_names.txt', 'r') as f:
    names_list = f.readlines()
starting_letter = ''.join(starting_letter)
print(starting_letter)
for name in names_list:
    name = name.strip()
    with open(f'./Output/ReadyToSend/letter_for_{name.strip()}.doc', 'w') as f:
        f.write(starting_letter.replace('[name]',name))


