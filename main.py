# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_file = "./Input/Names/invited_names.txt"
letter_file = "./Input/Letters/starting_letter.txt"

with open(names_file, mode="r") as file:
    name_list = file.readlines()

# with open(letter_file, mode="r") as file:
#     letter = file.readlines()

print(name_list)

for names in name_list:
    names = names.strip()
    with open(letter_file, mode="r") as file:
        letter = file.readlines()
    letter[0] = letter[0].replace("[name]", names)
    # print(letter)
    letter_content = ""
    for items in letter:
        letter_content += items

    with open(f"Output/ReadyToSend/{names}.txt", mode="w") as docu:
        docu.write(letter_content)
