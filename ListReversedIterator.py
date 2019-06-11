#!/usr/bin/env python3
my_input = input("Input string: ").split(' ')
print("Creating iteratable object: {}".format(reversed(my_input)))
print("Output string: ", end='')
for word in reversed(my_input):
    print(word, end=' ') # Print each word in reverse order with space in-between.
