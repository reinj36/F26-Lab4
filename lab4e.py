# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 11/10/2026
# Purpose: Modify the calcualtor program to use keyword parameters.
# Usage: ./lab4e.py

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
    userNum1 = int(input("Enter a number: "))
    userNum2 = int(input("Enter another number: "))
    userOperation = input("Enter an operation (+, -, *, or /): ")

    #call function with keyword parameters and store result in answer
    answer = compute(operation = userOperation, num1 = userNum1, num2 = userNum2)

    #print answer
    print("Result: ", answer)

if __name__ == "__main__" :
    main()