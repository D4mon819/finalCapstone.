#use input() command to ask for user's infomations

user_name = input('Please enter your name:')
user_age = input('Please enter your age:')
user_housenumber = input('Plesae enter your house number:')
user_Street = input('Please enter your street:')

#print the sentence with different variable in it

sentence = 'Hello ' + user_name + '!' + ' You are ' + user_age + ' years old and your address is house number ' + user_housenumber + ' on ' + user_Street + '.'

print(sentence)
