# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 9/10/2026
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py

# TO DO 1: Add the docstring
# @Function definition: add definition here
# @param: write parameters here
# @return: write return value here

# TO DO 2: Create the function.

def even_numbers(numbers) :
    
    """
    @Function definition: Finds all of the even numbers in a list.
    @param numbers: A list of numbers.
    @return: A list of even numbers.
    """

    evenList = []

    for number in numbers :

        #if number is even, append it to evenList
        if number % 2 == 0 :
            evenList.append(number)

    return evenList

# TO DO 3: Call the function.

myList = [2,5,8,9,13,4,5,1]
myListNoEven = [3,5,7,9,13,1,5,1]

#call function for list with even numbers
evenNumbers = even_numbers(myList)
print("New list (with even numbers):", evenNumbers)

#call function for list with no even numbers
evenNumbers = even_numbers(myListNoEven)
print("New list (without even numbers):", evenNumbers)

