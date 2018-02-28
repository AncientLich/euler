import math

result1 = 0
result2 = 0

for i in range(1,101):
    result1 = result1 + math.pow(i, 2)
    result2 = result2 + i
    
result2 = math.pow(result2, 2)

print(int(abs(result1 - result2)))