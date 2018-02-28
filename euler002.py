fibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
limit=4000000

couple = (55,89)

def valsave(couple):
    value = 0
    for x in couple:
        if x > value:
            value = x
    return value


while(couple[0]+couple[1] <= limit):
    new_value = couple[0] + couple[1]
    save_value = valsave(couple)
    couple = (save_value, new_value)
    fibonacci.append(new_value)


even_fibonacci = []
for x in fibonacci:
    if x % 2 == 0:
        even_fibonacci.append(x)

result = 0
for x in even_fibonacci:
    result += x

print(result)
