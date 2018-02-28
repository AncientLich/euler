import math

xa, xb, xc = (0,0,0)

solved = False
for a in range(2,1000):
    for b in range(a+1, 1000):
        c = math.sqrt((a*a) + (b*b))
        if float(a) + float(b) + c == 1000:
            solved = True
            xa, xb, xc = (a,b,c)
            break
    if solved:
        break

if solved:
    print(xa*xb*xc)
else:
    print('euler failed')
        