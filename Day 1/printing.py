# Instructions
# Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python 
# print function.
#
# Example Output
# After you have written your code, you should run your program and it should print the following:
# 
# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')

from wsgiref.validate import InputWrapper


print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
print()
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")
print()

# Instructions
# Look at the code in the code editor on the right. There are errors in all of the lines of code. Fix the code so that it runs without errors.
# 
# Warning: The output in your program should match the example output shown below exactly, character for character, even spaces and symbols should be identical, otherwise the tests won't pass.
# 
# Example Output
# When you run your program, it should print the following:
# 
# Day 1 - String Manipulation
# String Concatenation is done with the "+" sign.
# e.g. print("Hello " + "world")
# New lines can be created with a backslash and n.

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
print()

# Instructions
# Write a program that prints the number of characters in a user's name. You might need to Google for a function that 
# calculates the length of a string.

# e.g.
# https://www.google.com/search?q=how+to+get+the+length+of+a+string+in+python+stack+overflow
# Warning. Your program should work for different inputs. e.g. any name that you input.
# 
# Example Input
# Angela
# Example Output 
# 6

print(len(input("What is your name? ")))