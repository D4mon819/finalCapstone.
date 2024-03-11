#define the total number and how many numbers user have entered, make sure they are reset every time when programm start.

num_total = 0
numbers_entered = 0

#ask user to enter number
print("Enter a number,enter '-1' to stop and calculate the average you have entered:")

#start of the loop, set a limit of 100 in case it loop of infinity.
while numbers_entered < 100 :

    num = int(input())

    if num == -1 :                          #if user entered '-1', loop stop
        break
    num_total += num                        #add up the number and count the time entered
    numbers_entered += 1
if numbers_entered > 0:
    average = num_total / numbers_entered   #when the loop end, calculate avcerage and print
    print(f"Current average is {average}.")
else:                                       #If no valid numbers were entered, it will display an appropriate message.
    print("No valid numbers entered.")