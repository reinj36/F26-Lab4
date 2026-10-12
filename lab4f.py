# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 11/10/2026
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py

# Follow the instructions from readme.md.

def get_initials(*args) :

    """
    @Function definition: Extracts the first element from each argument.
    @param *args: Any number of parameters.
    @return: List of first elements from each argument.
    """

    #create list to hold initials
    initials = []

    #for each argument, append the element at the first index to initials
    for arg in args :
        initials.append(arg[0])

    return initials

def main() :

    #call get_initials for names given in instructions
    my_list = get_initials("Alice", "Bob", "Charlie", "David")

    #print returned list of initials
    print("Initials:", my_list)


if __name__ == "__main__" :
    main()