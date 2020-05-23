# Dita's Puzzle Generator
Based on a game of numbers presented to me by Dita Hollmannova, I decided to create an cellular automata to visualize the patterns.

Author: Sebastian Garcia, eldraco@gmail.com

The game was to find the next line in the sequence. For example:

		6
		61
		6111
		6113
		611231
		6112213111
		?

# Usage
To use the tool, pass the seed or initial number with -s, and optionally you can select the amount of lines with -l and width of the numbers with -w.
If you pass -p you will plot the png file, and if you pass -P you will print the lines

# Help

		✗ ./puzzle-generator.py -h
		Dita's Puzzle Generator. Version 0.1
		Author: eldraco@gmail.com

		usage: puzzle-generator.py [-h] [-v VERBOSE] [-l LINES] [-w WIDTH] [-s SEED]
								   [-p] [-P]

		optional arguments:
		  -h, --help            show this help message and exit
		  -v VERBOSE, --verbose VERBOSE
								Amount of verbosity. This shows more info about the
								results.
		  -l LINES, --lines LINES
								Amount of lines to generate.
		  -w WIDTH, --width WIDTH
								Width of the lines.
		  -s SEED, --seed SEED  Initial line of numbers.
		  -p, --plot            To plot or not in a png file.
		  -P, --print           Print the numbers in console.

# Plots

In order to plot the sequence we assign a color to each number from 0 to 9, and then we assign a pixel to each number. 
We pad the rows to have a min and max width with 0 (white).


# Example

## Seed 6, only print

		✗ ./puzzle-generator.py -s '6' -l 10 -w 100 -P
		Dita's Puzzle Generator. Version 0.1
		Author: eldraco@gmail.com

		Lines to print: 10
		Numbers per line: 100
		Using seed: 6

		Iteration number: 0: 6
		Iteration number: 1: 61
		Iteration number: 2: 6111
		Iteration number: 3: 6113
		Iteration number: 4: 611231
		Iteration number: 5: 6112213111
		Iteration number: 6: 611222113113
		Iteration number: 7: 61122312311231
		Iteration number: 8: 6112223111213112213111
		Iteration number: 9: 61122331132111311222113113

## Generate a plot with seed 111222333444555666777888999000

		./puzzle-generator.py -s '111222333444555666777888999000' -l 50 -w 300; imgcat ditomata.png
		Dita's Puzzle Generator. Version 0.1
		Author: eldraco@gmail.com

		Lines to print: 50
		Numbers per line: 300
		Using seed: 111222333444555666777888999000


![Example of Seed 111222333444555666777888999000](https://github.com/eldraco/ditas-number-generator/raw/master/ditomata-111222333444555666777888999000.png "Example of Seed 111222333444555666777888999000")


## Generate a plot with seed 93485739475938475

		./puzzle-generator.py -s '93485739475938475' -l 50 -w 300; imgcat ditomata.png
		Dita's Puzzle Generator. Version 0.1
		Author: eldraco@gmail.com

		Lines to print: 50
		Numbers per line: 300
		Using seed: 93485739475938475

![Example of Seed 93485739475938475](https://github.com/eldraco/ditas-number-generator/raw/master/ditomata-93485739475938475.png "Example of Seed 93485739475938475")
