#!/usr/bin/env python

line_to_print = '661'
print(f'{line_to_print}')

while line_to_print:
    # Get each number in the line
    line = line_to_print
    line_to_print = ''

    number_index = 0
    # i starts in 1 so we dont count the 'number' twice. counter is 1 too
    internal_index = 1
    while number_index < len(line):
        number = line[number_index]
        # Add the next number to print
        line_to_print += number
        # The number appears at least once
        counter = 1
        while internal_index < len(line):
            # Since i starts in 1 instead of 0, the comparision is against line[i] instead of line[i + 1]
            if line[internal_index] == number:
                counter += 1
                internal_index += 1
            else:
                # There are no more equal numbers, go out
                break
        # The current number we need to print the count
        line_to_print += str(counter)
        # We need now to continue with the rest of the numbers in this line
        # if i > len(line) there are no more numbers to process, if i <= len(line) we need to continue
        if internal_index <= len(line):
            number_index = internal_index - 1

    line = line_to_print
    print(f'{line}')




