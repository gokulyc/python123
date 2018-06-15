print("Hi1")
a = 10
print(10)

a = [1, 2, 3, 4, 5]
a.sort(reverse=True)
for i in a:
    print(i)

import math

print(dir(math))

from string import whitespace

print("dfbhjvsfhs" + whitespace + str(math.sqrt(1024)))

import sys

print(sys.version)
print(sys.argv)

import os

print(os.getcwd())
print(os.chdir("G://Desktopchai"))

print(os.getcwd())
'''os.mkdir("G://Desktopchai//edu")
#os.remove(path of file) removes the file in pah

a=input("enter to continue")

os.rmdir("G://Desktopchai//edu")
'''
import random

print(random.randrange(50.0))

print(random.randrange(0, 50.0, 10))

print(random.randint(0, 50))

print(int(10 * random.random()))

import datetime

print(datetime.datetime.today())
now = datetime.datetime.today()
oth = datetime.datetime(1993, 11, 20, 22, 00)
print(now - oth)

import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3}]

print(repr(data))

data_str = json.dumps(data)
print("dumps", data_str)
decoded = json.loads(data_str)
print("Decoded", decoded)

# tuple to list and stirng to unicode

print("original ", type(data[0]['b']))
print("decoded ", type(decoded[0]['b']))
