"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# # No setup
# repeat forever:
def my_calculator():
	while True:
		raw_input = input(">")
		split_input = raw_input.split(" ")

		for i in range(1,len(split_input)):
			split_input[i] = float(split_input[i])

		if split_input[0] == "q":
			break
		else:
			if split_input[0] == "+":
				print (add(split_input[1],split_input[2]))
			elif split_input[0] == "-":
				print (subtract(split_input[1], split_input[2]))
			elif split_input[0] == "*":
				print (multiply(split_input[1], split_input[2]))
			elif split_input[0] == "/":
				print (divide(split_input[1], split_input[2]))				
			elif split_input[0] == "square":
				print (square(split_input[1]))
			elif split_input[0] == "cube":
				print (cube(split_input[1]))
			elif split_input[0] == "pow":
				print (power(split_input[1], split_input[2]))
			elif split_input[0] == "mod":
				print (mod(split_input[1], split_input[2]))

my_calculator()
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token

# Your code goes here
