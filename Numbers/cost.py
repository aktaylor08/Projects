#!/usr/bin/env python
import sys

width = input('Room Width: ')
height = input('Room Height: ')
cost = input('Cost Per square foot: ')

width = float(width)
height = float(height)
cost = float(cost)

print 'The cost is {0}'.format(width * height * cost)
