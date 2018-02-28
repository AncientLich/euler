# This is the first code I try. It is a bruteforce method.
# This method works fine to calculate all patterns until 10x10 in short times.

# This bruteforce was useful to generate data in euler015_deb.txt, wich I 
# analized in order to find a way to calculate lattice patterns without
# bruteforce method (see euler015.py)



class Path():
    def __init__(self, x, y, limit):
        self.x = x
        self.y = y
        self.limit = limit
    
    def __str__(self):
        return '({},{}) | {}'.format(self.x, self.y, self.test_complete())
    
    def generate(self):
        return (Path(self.x+1, self.y, self.limit), 
                Path(self.x, self.y+1, self.limit))
    
    def iscomplete(self):
        if self.x >= self.limit[0] or self.y >= self.limit[1]:
            return True
        else:
            return False
    
    def test_complete(self):
        if self.iscomplete():
            return "(complete)"
        else:
            return ""



with open('euler015_deb.txt', 'w', encoding='utf-8') as fo:
    for x in range(1,11):
        print('-----------------', file=fo)
        for y in range(1,11):
            print('{}X{}....'.format(x, y))
            poplist = None
            poplist = [Path(0, 0, (x, y))]
            routes = 0
        
            while poplist is not None:
                new_poplist = None
                for i in poplist:
                    path1, path2 = i.generate()
                    for path in (path1, path2):
                        if path is not None:
                            if path.iscomplete():
                                routes += 1
                            else:
                                if new_poplist is None:
                                    new_poplist = []
                                new_poplist.append(path)
                poplist = new_poplist
            
            print('({}, {}) --> {}'.format(x, y, routes), file=fo)

