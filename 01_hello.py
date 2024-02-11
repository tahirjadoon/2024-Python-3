#!/usr/bin/python3
#hello.py sample to say hello

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
"""

import sys

# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'World'
  print('Hello', name)
  print(' ')
  print(' ')

# This is the standard boilerplate that calls the main() function.
print('Printing __name__ : ', __name__)
print('-' * 20)
print('Printing sys.argv : ', (sys.argv))
print('-' * 20)

if __name__ == '__main__':
  main()
