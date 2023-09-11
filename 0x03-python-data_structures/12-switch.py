#!/usr/bin/python3
a = 89
b = 10
temp1 = a
temp2 = b
del a
del b
a = temp2
b = temp1

print("a={:d} - b={:d}".format(a, b))
