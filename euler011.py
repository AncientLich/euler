matrix = []
lenlist = 0

with open('euler011.src', 'r', encoding='utf-8') as fi:
    for xline in fi:
        xline = xline.strip('\r\n')
        row = xline.split(' ')
        mylist = None
        mylist = []
        for val in row:
            mylist.append(int(val))
        matrix.append(mylist)
        lenlist = len(mylist)

result = 1


def calc_nums(matrix, start, progression):
    values = None
    values = []
    for i in range(0,4):
        x = start[0] + (progression[0] * i)
        y = start[1] + (progression[1] * i)
        try:
            values.append(matrix[x][y])
        except IndexError:
            return (1,1,1,1)
    return values
    

def checker(matrix, start, progression, result):
    num1, num2, num3, num4 = calc_nums(matrix, start,  progression)
    if num1*num2*num3*num4 > result:
        return num1*num2*num3*num4
    else:
        return result


for progression in [(1,0),(0,1),(1,1),(1,-1)]:
    for x in range(0,lenlist):
        for y in range(0, len(matrix)):
            result = checker(matrix, (x,y), progression, result)

print(result)


# -------------------------------------------

''' codice di il_ratto

COUNT = 4


def segments(grid, count):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            for dirx, diry in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                try:
                    yield reduce(lambda x, y: x * y, (grid[x+dirx*i][y+diry*i] for i in range(count)))
                except IndexError:
                    pass

print(max(segments(GRID, COUNT)))

'''
