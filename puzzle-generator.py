#!/usr/bin/env python
# Python implementation of the game sent by dita of finding which is the next sequence in
# 6
# 61
# 6111
# 6113
# 611231
# After finding the sequence, this is the generator i did
# Author: Sebastian Garcia, eldraco@gmail.com
import png
import argparse
from PIL import Image

def generate_plot_line(line):
    """
    Generate the plot line for this line of numbers
    """
    # Chop line to our max width
    line = line[:line_width]
    # Pad the line with 0 in case is shorter than line_width
    line += '0' * (line_width - len(line))

    temp_tuples = ()
    for number in line:
        num_tuple = colors[number]
        temp_tuples += num_tuple
    plot_line.append(temp_tuples)

if __name__ == '__main__':
    print(f'Dita\'s Puzzle Generator. Version 0.1')
    print('Author: eldraco@gmail.com\n')

    colors = {'0': (255, 255, 255), # White
              '1': (255, 0, 128),   # pink
              '2': (127, 0, 255),   # violet
              '3': (0, 0, 255),     # Blue
              '4': (0, 255, 255),   # cyan
              '5': (0, 255, 128),   # green
              '6': (255, 255, 0),   # yellow
              '7': (255, 128, 0),   # orange
              '8': (255, 0, 0),     # red
              '9': (0, 0, 0)}       # Black
    plot_line = []

    # Parse the parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='Amount of verbosity. This shows more info about the results.', action='store', required=False, type=int)
    parser.add_argument('-l', '--lines', help='Amount of lines to generate.', action='store', required=False, type=int, default=500)
    parser.add_argument('-w', '--width', help='Width of the lines.', action='store', required=False, type=int, default=1000)
    parser.add_argument('-s', '--seed', help='Initial line of numbers.', action='store', required=False, type=str)
    parser.add_argument('-p', '--plot', help='To plot or not in a png file.', action='store_true' , required=False, default=False)
    parser.add_argument('-P', '--print', help='Print the numbers in console.', action='store_true' , required=False, default=False)
    args = parser.parse_args()


    # how many lines
    if args.lines:
        iterations = args.lines
    else:
        # Default amount of lines we generate
        iterations = 500
    amount_of_lines = iterations

    # Max amount of positions in a line. Both to generate and plot
    if args.width:
        line_width = args.width
    else:
        line_width = 1000

    # This is the default seed line
    if args.seed:
        line_to_print = args.seed
    else:
        line_to_print = '6'


    print(f'Lines to print: {iterations}')
    print(f'Numbers per line: {line_width}')
    print(f'Using seed: {line_to_print}')
    print()

    while line_to_print and iterations:
        if args.print:
            print(f'Iteration number: {amount_of_lines - iterations}: {line_to_print}')
        line = line_to_print[:line_width]
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
        generate_plot_line(line_to_print)
        iterations -= 1

    # Plot
    f = open('ditomata.png', 'wb')
    w = png.Writer(line_width, amount_of_lines, greyscale=False)
    w.write(f, plot_line)
    f.close()

    img = Image.open('ditomata.png')

    basewidth = 2000
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))

    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save('ditomata.png', "PNG")
