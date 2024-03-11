# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")                       # Syntax errors, missing parenthesis after print command.
print("\n")                                                 # Syntax errors and compilation error, missing parenthesis after print command and this line do not need indented statements.

    # Variables declaring the user's age, casting the str to an int, and printing the result
# Compilation error, line 10 to 16 do not need indented statements.
age_Str = "24"                                              # Runtime error, age_Str need = to define
age = int(age_Str)                                          # Runtime error, age_Str contain word so it cannot change to integer.
print(f"I'm {age} years old.")                              # Syntax errors, 'age' is a integer and  required for f-string formatting to print.

    # Variables declaring additional years and printing the total years of age
years_from_now = 3
total_years = age + years_from_now                          # Syntax error, 'years from now' should be a integer.

print(f"The total number of years: {total_years} ")         # Syntax errors, missing parenthesis after print command, '"answer_years"' should be 'total_years' and use f-string to print integer.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12                             # Syntax error, 'total' should be 'total_years'.
print("In 3 years, I'll be " + str(total_months) + " months old") # Syntax errors and logical errors, missing parenthesis after print command, 'total_months' should change into str and it should be 3 years not 3 years and 6 months.

#HINT, 330 months is the correct answer

