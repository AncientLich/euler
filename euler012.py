import math


def is_prime(x, primes):
    if x < 2:
        return False
    elif x in primes:
        return True
    else:
        try:
            maxprime = max(primes)
        except ValueError:
            # 1 is not actually a prime. But when primes is still empty,
            # (when ValueError raised) we must start range from value 2
            # to ensure this we must state that maxprime is 1 in order to let
            # 'range' in 'for n in range' to start from 2
            maxprime = 1
        if x < maxprime:
            return False
        else:
            for n in range(maxprime +1,x):
                if x % n == 0:
                    return False
            return True



def calcprimes(size):
    amount = 0
    value = 1
    primes = set()
    while amount < size:
        if is_prime(value, primes):
            amount += 1
            primes.add(value)
        value += 1
    return primes



def updateprimes(new_limit, primes):
    for x in range(max(primes) +1, new_limit +1):
        if is_prime(x, primes):
            primes.add(x)
    return primes



def calc_divisors_and_updprimes(value, primes):
    sqval = math.ceil(math.sqrt(value))
    primes = updateprimes(sqval, primes)
    # divisors start from 1, becouse 1 is not a prime, but every number can be
    # divided by 1
    divisors = 1
    for prime in primes:
        if prime > sqval:
            break
        elif value % prime == 0:
            divisors += 1
    divisors = divisors * 2
    return (divisors, primes)



class Triangular:
    def __init__(self):
        self.value = 0
        self.adder = 1
    
    def __next__(self):
        self.value += self.adder
        self.adder += 1
        return self


# ----------------------------------------------------------------------------


tri = Triangular()
primes = calcprimes(1500)

while True:
    next(tri)
    divisors, primes = calc_divisors_and_updprimes(tri.value, primes)
    if divisors > 500:
        break

print('[divisors are: {}]'.format(divisors))
print('result is', tri.value)
