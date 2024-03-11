import  math

#Instruction and ask user to enter the type.
print('''
investment  - to calculate the amount of interest you'll earn on your investment
bond        - to calculate the amount you'll have to pay on a home loan
''')
type = input("Enter either 'investment' or 'bond' from the menu above to proceed:")


if type.lower() == 'investment' :                                                                           #Investment calculator, ask user to enter info and kind of interest
    p = float(input("Enter the amount of money that you are depositing: \n"))
    r = float(input("Enter the % of the interest (numbers only):\n"))/100
    t = int(input("Enter the number of years you want to deposit\n"))
    interest = input("Enter the 'simple' or 'compound' interest:\n").lower()

    if interest == 'simple' :                                                                               #Simple interest calcualtion and result
        total_amount = p*(1+r*t)
        print(f"The total amount after {t} years at {r * 100}% {interest} interest is: {total_amount}")

    elif interest == 'compound' :                                                                           #Compound interest calculation and result
        total_amount = p*math.pow((1+r),t)
        print(f"The total amount after {t} years at {r * 100}% {interest} interest is: {total_amount}")

    else :                                                                                                  #Prevent user did not enter anything
        print("Invalid interest type. Please enter 'simple' or 'compound'.")

elif type.lower() == 'bond' :                                                                               #Bond calculator, ask user to enter info
    p = float(input("Enter the amount of money that you are depositing: \n"))
    r = float(input("Enter the % of the interest (numbers only):\n")) / 100/12
    t = int(input("Enter the number of months you want to deposit\n"))

    repayment = (r * p) / (1 - (1 + r) ** (-t))                                                             # Bond calculation and result
    print(f"The monthly repayment amount for the bond is: {repayment}")

else:
    print("Error! Enter either 'investment' or 'bond' from the menu above to proceed")                      #Prevent user did not input type








