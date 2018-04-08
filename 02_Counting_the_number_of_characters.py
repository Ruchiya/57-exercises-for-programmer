"""
Exercise 02:

Create a program that prompts for an input string and displays output that shows the input string and the number of
characters the string contains.

"""

while True:
    string = input('What is the input string?:')
    char = string.replace(' ','')
    if string=='':
        continue
    else:
        print(f'"{string}" has {len(char)} characters.')
        break
