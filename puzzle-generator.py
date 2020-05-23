#!/usr/bin/env python
# Python implementation of the game sent by dita of finding which is the next sequence in
# 6
# 61
# 6111
# 6113
# 611231
# After finding the sequence, this is the generator i did
# Author: Sebastian Garcia, eldraco@gmail.com

iterations = 20
# Start with this line
line_to_print = '6'
# The first line should be printed manually
print(f'{line_to_print}')

while line_to_print and iterations:
    line = line_to_print
    line_to_print = ''
    # The index of the 'main' numbers that do not repeat, the numbers to search for
    number_index = 0
    # Internal index while searching for repeated numbers
    internal_index = 0
    while number_index < len(line):
        # Get the current main number
        number = line[number_index]
        # Add the next number to print
        line_to_print += number
        # The number of times the main number appears
        counter = 0
        while internal_index < len(line):
            # Is the main number repeated once more?
            if line[internal_index] == number:
                counter += 1
                internal_index += 1
            else:
                # There are no more equal numbers, go out
                break
        # The current number we need to print the count
        line_to_print += str(counter)
        # We need now to continue with the rest of the main numbers in this line, if there are any
        number_index = internal_index
    print(f'{line_to_print}')
    iterations -= 1

