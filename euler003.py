#! /usr/bin/env python3

import math

limit=600851475143

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
               return False
        return True


value = int(math.sqrt(limit))

encountered = False

while encountered is False:
    if limit % value == 0:
        if is_prime(value):
            break
    value -= 1

print(value)