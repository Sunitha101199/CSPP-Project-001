"""Implementing the cat shell command in python."""

import sys
from lib.helper import cat, readfile

TEXT = None #TEXT is a variable assigned a null value.
ARG_CNT = len(sys.argv) - 1 #ARG_CNT is a variable with an int value. 

if ARG_CNT == 0:
    TEXT = sys.stdin.read()

if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)

if ARG_CNT > 1:
    print(sys.argv[0], "doesn't handle more than one argument")

print(cat(TEXT))

