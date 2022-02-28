
import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    pairs = { "(": ")", "[": "]", "{": "}" }
    stack = []

    for character in s:
      if(not stack):
        stack.append(character)
      elif(character == pairs.get(stack[-1])):
        stack.pop()
      else:
        stack.append(character)

    return 'YES' if not stack else 'NO'


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result + '\n')

