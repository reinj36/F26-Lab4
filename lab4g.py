# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 11/10/2026
# Purpose: Practice map, filter and lambda expressions.
# Usage: ./lab4g.py

# Follow the instructions from readme.md.

#variables
numbers = [2,3,4,5,6,7,8,9,10]
divisible_by_2 = []

#print original list
print("Original list:", numbers)

#square all elements of numbers and print
square_lambda = lambda num : num ** 2
numbers = list(map(square_lambda, numbers))

print("Squared list:", numbers)


#filter elements of numbers that are divisible by 2 and print
divide_lambda = lambda num : num % 2 == 0 #filter would filter based on if element % 2 == 0
divisible_by_2 = list(filter(divide_lambda, numbers)) #remember to convert result to list

print("Filtered list:", divisible_by_2)