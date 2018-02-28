import math

def calc_factors(num, primes):
    while num not in primes:
        for i in sorted(primes):
            if num % i == 0:
                yield i
                num = num / i
                break                
    if(num != 1):
        yield num



def group_factors(factors):
    value = {}
    for val in factors:
        if val in value:
            value[val] += 1
        else:
            value[val] = 1
    return value



def update_factory(factory, groups):
    for factor, times in groups.items():
        if times > factory[factor]:
            factory[factor] = times

# --- obtaining prime factors within first 20 numbers ---


limit=20

primes=set()
seeker=2



for a in range(2,limit):
    primes.add(a)


while (seeker*seeker < limit):
    mul = 2
    while (seeker*mul < limit):
        try:
            primes.remove(seeker*mul)
        except KeyError:
            pass
        mul += 1
    for a in sorted(primes):
        if a > seeker:
            seeker = a
            break

# ------- collecting prime factors and final calc ----

factory = {}

for i in primes:
    factory[i] = 1

for i in range(4,21):
    factors = calc_factors(i, primes)
    if factors is not None:
        groups = group_factors(factors)
        update_factory(factory, groups)
        

result = 1
for factor, times in factory.items():
    result = result * int(math.pow(factor, times))

print('result is', result)