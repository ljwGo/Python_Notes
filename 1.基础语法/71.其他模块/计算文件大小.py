#! /usr/bin/env python3.8
import os
import os.path
import sys

abs_file = sys.argv[1]

def my_getsize(file,x=''):
    total = 0
    file = os.path.join(file, x)
    for x in os.listdir(file):
        if os.path.isdir(os.path.join(file,x)):
            my_getsize(file,x)
        else:
            file_name = os.path.join(file, x)
            with open('{}'.format(file_name), mode='rb') as f:
                for line in f:
                    total += len(line)
    return total

print(my_getsize(abs_file))
