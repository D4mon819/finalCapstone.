# ask user to enter a sentence, save it as a string and call it in str_manip
str_manip = str(input('Please enter a sentence:'))


#calculate the length of string by using len() and print it out
print(len(str_manip))

#Find out and save the last letter
lastletter = str_manip[-1]

#Replace all every occurrence of last letter with @ and print
str_manip_replace = str_manip.replace( lastletter, '@')
print(str_manip_replace)


#print last 3 letter backward with :-4:
print(str_manip[:-4:-1])

#store first 3 and last 2 letter
first_3_chara = str_manip[:3:]
last_2_chara = str_manip[-2::]

#Creat the new world and print it out
print(first_3_chara+last_2_chara)