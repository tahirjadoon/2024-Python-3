#!/usr/bin/python3 -tt

import sys
import os
#

#sys.path.append('../')
#sys.path.append('/Python2024/PY_01BasicExamples')
sys.path.insert(0, os.path.relpath('/Python2024/PY_01BasicExamples'))
print(sys.path)

#from ...Python2024.PY_01BasicExamples.functions1_simple import *
#from PY_01BasicExamples import functions1_simple as f1s
import PY_01BasicExamples.functions1_simple as f1s

def main():
  #functions1_simple.printHeader("Any") #coming from functions1_simple
  f1s.printHeader("Any")
  print("Hi")

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()