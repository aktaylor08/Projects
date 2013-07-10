#!/usr/bin/env python
import sys

def fib(n):
    '''calculate the fibanatci sequence up to the nth number'''
    count = 0
    b, a = 0,1
    while count < n:
        print a
        temp = a+b
        b = a
        a = temp
        count += 1
        
if __name__ == '__main__':
    print sys.argv
    fib(int(sys.argv[1]))

