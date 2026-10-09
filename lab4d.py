# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 9/10/2026
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

# Follow the instructions from readme.md.

#performs a calculation inputted by user on two numbers inputted by user
def compute(num1, num2, operation = '+') :
    if operation == '+':
        return num1 + num2
    elif operation == '-' :
        return num1 - num2 
    elif operation == '/' :
        if num2 == 0:
            return "Error. Cannot divide by 0."
        else:
            return num1 / num2 
    elif operation == '*':
        return num1 * num2
    else:
        return num1 + num2

def main() :

    #get two numbers and operation from user
    num1 = "Enter a number:"
    num2 = "Enter another number:"
    operation = "Enter an operation (+, -, *, or /):"

    #call function and store result in answer
    answer = compute(num1, num2, operation)

    



