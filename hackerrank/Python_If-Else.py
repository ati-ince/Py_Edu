#!/bin/python3

import math
import os
import random
import re
import sys

even= 2%2
odd = 1%2

def weird():
    print("Weird")

def n_weird():
    print("Not Weird")

def nop():
    pass

if __name__ == '__main__':
    n = int(input().strip())

    if n%2 is odd:
        weird()
    elif n%2 is even:
        if n>=2 and n<=5:
            n_weird()
        elif n>=6 and n<=20:
            weird()
        elif n>20:
            n_weird()
        else:
            nop()


#TASK
'''
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
Explanation 1


 and  is even, so it is not weird.

 '''