string = input("Please enter a string: \n")
alternate_characters = ''
for i in range(len(string)):
    if i % 2 == 0:
        alternate_characters += string[i].upper()
    else:
        alternate_characters += string[i].lower()

print("Alternate Characters:", alternate_characters)

words = string.split()
result_words = ''
for i, word in enumerate(words):
    if i % 2 == 0:
        result_words += word.lower()
    else:
        result_words += word.upper()
    result_words += ' '  # Add space between words

print("Alternate Words:", result_words.strip())