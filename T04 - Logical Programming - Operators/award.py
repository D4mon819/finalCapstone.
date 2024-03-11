# Introduce program and ask user to enter their data, since the time is count in minute, therefore we need float instead of integer.
print("This is a program that determines what award you will get after competing in a triathlon.")
swimming_time = float(input("Please enter your swimming time (in mins): \n"))
running_time = float(input("Please enter your running time (in mins): \n"))
cycling_time = float(input("Please enter your cycling time (in mins): \n"))

# Calculate the total time.
total_time = swimming_time+running_time+cycling_time


# Use if elif else command to determine the award user get, from most taken time to lowest taken time.
if total_time >= 111 :
    print(f"Thank you for joinning! Your total time taken in triathlon is {total_time} minutes. \nUnfortunately you get no reward this time. Try harder next time!")

elif total_time >= 106 :
    print(f"Congratulation! Your total time taken in triathlon is {total_time} minutes. You have won Provincial Scroll.")

elif total_time >= 101 :
    print(f"Congratulation! Your total time taken in triathlon is {total_time} minutes. You have won Provincial Half Colours.")

elif total_time > 0 :
    print(f"Congratulation! Your total time taken in triathlon is {total_time} minutes. You have won Provincial Colours.")

else:
    print("Please enter a valid time")




