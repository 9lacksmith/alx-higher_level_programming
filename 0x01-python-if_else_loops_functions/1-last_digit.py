#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < -1:
    lstDgt = abs(number) % 10
else :
    lstDgt = number % 10

if lstDgt > 5:
    print("Last digit of {} is {} and is greater than 5".format(number,
          lstDgt))
elif lstDgt == 0:
    print("Last digit of {} is {} and is 0".format(number, lstDgt))
elif (lstDgt < 6) and (lstDgt != 0) :
    print("Last digit of {} is {} and less than 6 and not 0".format(number,
          lstDgt))
