#!/usr/bin/env python3
my_input = input("Input string: ").split(" ")
# Split string into list by-spaces.

my_input.reverse()
# This method returns None but reverses the list in-place.

print("Output string: {}".format(" ".join(my_input)))
# Print the reversed output, join/concatenate items with a space in-between.
