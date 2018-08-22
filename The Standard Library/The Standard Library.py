#Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.

import random

a=random.randint(0,1)
b=random.randint(1,10)

print(a)
print(b)

#Use the datetime library together with the random number to generate a random, unique value.

import datetime

c = str(datetime.datetime.now()) + str(b)
print(c)