#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

#calculate last digit
if number < 0:
    calc = number * -1
else:
    calc = number
lastdigit = calc % 10

#evaluate last digit
if lastdigit > 5:
    print('Last digit of %d is %d and is greater than 5' % (number, lastdigit))
elif lastdigit == 0:
    print('Last digit of %d is %d and is 0' % (number, lastdigit))
elif lastdigit < 6:
    print('Last digit of %d is %d and is less than 6 and not 0'
          % (number, lastdigit))
