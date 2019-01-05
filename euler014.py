def gen2(limit):
    value = 1
    exp = 0
    while value <= limit:
        value = value * 2
        exp += 1
        yield (value, exp)




exp2 = dict(gen2((999999 * 3)+1))


longer_chain = (0, 0)

for v in range(1, 1000000):
    chain = 1 
    endchain = False
    value = v
    while not endchain:
        chain += 1
        if value % 2 == 0:
            value = int(value /2)
        else:
            value = (value * 3) +1
            if value in exp2.keys():
                chain += exp2[value]
                endchain = True
            
    if chain > longer_chain[0]:
        longer_chain = (chain, v)
    
    if v == 13:
        print('chain length for 13:', chain)

print('''longest chain is {}
provided by value: {}'''.format(longer_chain[0], longer_chain[1]))

