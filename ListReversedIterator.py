#!/usr/bin/env python3
my_input = input("Input string: ").split(' ')
reversed_input = reversed(my_input)
print("Created iteratable object: {}".format(reversed_input))
print("Output string: ", end='') # No trailing newline.
for word in reversed_input:
    print(word, end=' ') # Print each word in reverse order with space in-between.
