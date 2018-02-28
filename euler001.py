limit=1000

values = set([3,5])

for x in (3,5):
    mul = 2
    while(x*mul < limit):
        values.add(x*mul)
        mul +=1

result = 0

for x in values:
    result += x

print(result)
