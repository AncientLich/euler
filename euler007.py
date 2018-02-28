def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
               return False
        return True

counter = 0
value = 1
result = 0

while(counter < 10001):
    print('testing: ', counter)
    if is_prime(value):
        result = value
        counter += 1
    value += 1

print('result =', result)