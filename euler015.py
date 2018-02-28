# Lattice Path calculator (euler 15)

# Observing values from bruteforce (euler015_dbg.py), I noticed:
# sequence 1,? is (1,1) = 1+1 = 2 ==> with progression +1 for each following element
# sequence n,? (where n is > 1) is:
#     (n,1) = n+1  (starting value)
#     progression for next values is an additional value wich is calculated from the
#     preceding (n-1, ?) values starting from second element value for first addition:
#     example:
#     (1,1) = 2;  (1,2) = 3; (1,3) = 4;
#     than (2,x) will be:
#     (2,1) = 3; [first value is 2+1, as in 1,x sequence]
#     (2,2) = 3 + (1,2) = 3 + 3 = 6
#     (2,3) = 6 + (1,3) = 6 + 4 = 10
#     than (3,x) will be:
#     (3,1) = 4; [usual first value]
#     (3,2) = 4 + (2,2) = 4 + 6 = 10
#     (3,3) = 10 + (2,3) = 10 + 10 = 20
#     than (4,x) will be:
#     (4,1) = 5
#     (4,2) = 5 + (3,2) = 5 + 10 = 15
#     (4,3) = 15 + (3,3) = 15 + 20 = 35
# etc

# As you can see, with this approach we can calculate lattice paths (x,y)
# knowing lattice paths (x-1, y) and (x, y-1)
# this is also the reason why latticeCalc will sort x,y so x <= y so we have
# an odered way to approach, allowing us to feed starting (1,n) values and
# allowing us to be sure that y will always have at least 2

# 

def new_lattice(prev_lattice):
    lattice = None
    lattice = []
    for i in prev_lattice:
        if i == prev_lattice[0]:
            lattice.append(prev_lattice[0] +1)
        else:
            lattice.append(lattice[-1] + i)
    return lattice



def latticeCalc(xx, yy):
    x, y = sorted([xx, yy])
    # the first value is actually useless, but we keep it.
    prev_lattice = list(map(lambda q: q+1, range(1, y+1)))
    lattice = list(prev_lattice)
    for i in range(2,x+1):
        # lattice = new_lattice(prev_lattice)
        lattice = None
        lattice = [prev_lattice[0]+1 if prev_lattice[0] == i else lattice[-1] + i for i in prev_lattice]
        prev_lattice = list(lattice)
    return lattice[-1]


print(latticeCalc(20,20))
