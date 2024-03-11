#ask user to enter their age between 1 to 100
age = int(input("Please enter your age (between 0 to 100):"))

#Check if user reall enter over 100, then check if user is 21, then check their age from old to young, if their age not match specific condition, it consider as any other age.
if age >= 100 :
    print("Sorry, you're dead.")

elif age == 21 :
    print("Congrats on your 21st!")

elif age >= 65:
    print("Enjoy your retirement!")

elif age > 40:
    print("You're over the hill.")

elif age < 13:
    print("You qualify for the kiddie discount.")

else :
    print("Age is but a number.")




