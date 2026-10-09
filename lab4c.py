# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Reina James
# Date: 9/10/2026
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

# Follow the instructions from readme.md.

#calculate sum of two numbers in a function
def sum(num1, num2) :

    """
    @Function definition: Calculates the sum of two numbers.
    @param num1, num2: Two numbers.
    @return: The sum of the two numbers.
    """

    return num1 + num2


#main function
def main() :
    
    #get user input for 2 numbers
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    numberSum = sum(num1, num2)

    print("Sum:", numberSum)


if __name__ == "__main__" :
    main()

