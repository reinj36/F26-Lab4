# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 9/10/2026
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py

# TO DO 1: Add the docstring
# @Function definition: add definition here
# @param: write parameters here
# @return: write return value here 

# TO DO 2: define the function with name `is_even`.

def is_even(numbers) :

    """
    @Function definition: Checks if any number in the list is even.
    @param numbers: A list of numbers.
    @return: A boolean value.
    """

    #determines if false or true should be returned
    evenNotFound = True

    
    for number in numbers :

        #if the number is even, return true and set evenNotFound to false
        if number % 2 == 0 :
            return True
            evenNotFound = False

    #if there is no even number, return false
    if (evenNotFound) :
        return False

# TO DO 3: Call the function `is_even`.

myListOdd = [3,5,9,7,1,9]
myListEven = [3,5,9,4,1,9]

#call function for list with all odd values
evenFound = is_even(myListOdd)
print("Is there an even number? -->", evenFound)

#call function for list with an even value
evenFound = is_even(myListEven)
print("Is there an even number? -->", evenFound)