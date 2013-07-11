#!/usr/bin/env python
import sys

def fib():
    '''calculate the fibanatci sequence up to the nth number'''
    count = 0
    b, a = 0,1
    while 1:
        yield a
        temp = a+b
        b = a
        a = temp
        
if __name__ == '__main__':
    n = int(sys.argv[1])
    a = fib()
    for i in range(n):
        print a.next()

