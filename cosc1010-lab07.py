# Johnavon Jones
# UWYO COSC 1010
# Submission Date: 10/31/2024
# Lab 07
# Lab Section: 12
# Sources, people worked with, help given to:https://www.w3schools.com/python/ref_string_split.asp, https://flexiple.com/python/python-replace-character-in-string, Ryder Downey

# Prompt the user for an upper bound
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so

# You will continue to prompt the user until a proper integer value is entered
upper_bound = input("Input a number and I will calculate the factorial!:") 
factorial = 1
while not upper_bound.isnumeric():
    print("You didn't enter a number!")
    upper_bound = input("Input a upper bound.") 
upper_bound = int(upper_bound)

for i in range(1, upper_bound + 1):
        factorial *= i
print(f"The result of the factorial based on the given bound is {factorial}")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 
exit = False
leave_string = "exit"
num_sum = 0
while not exit:
    number = input("Input a number and I will add it together (Type exit to get your total):")
    if number.lower() == leave_string:
        exit = True
    elif number[0] == "-" or number[1:].isnumeric():
        num_sum += int(number)
    else:
        print("You typed something that wasn't a number!")
print(f"Your final sum is {num_sum}")
print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 
leave = False
leave_string = "exit"
while not leave:
    math_problem = input("Enter a problem with a sign(+,-,*,/,%)(Type exit to stop):")
    math_problem = math_problem.replace(" ", "")
    if math_problem.lower() == leave_string:
        leave = True
    elif "+" in math_problem:
        math_problem = math_problem.split("+")
        solution = int(math_problem[0]) + int(math_problem[1])
        print(f"The two numbers added together is {solution}")
    elif "-" in math_problem:
        math_problem = math_problem.split("-")
        solution = int(math_problem[0]) - int(math_problem[1])  
        print(f"The two numbers subtracted is {solution}")  
    elif "*" in math_problem:
        math_problem = math_problem.split("*")
        solution = int(math_problem[0]) * int(math_problem[1])
        print(f"The two numbers multiplied is {solution}") 
    elif "/" in math_problem:
        math_problem = math_problem.split("/")
        if int(math_problem[1]) == 0:
            print("Error: You can't divide by 0!")
        else:
            solution = int(math_problem[0]) / int(math_problem[1])
            print(f"The two numbers divided is {solution}") 
    elif "%" in math_problem:
        math_problem = math_problem.split("%")
        solution = int(math_problem[0]) % int(math_problem[1])
        print(f"The remainder of the two numbers divided is {solution}")
    else:
        print("You entered something that wasn't a number!")
        

        