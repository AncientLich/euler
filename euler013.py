class BNBlock:
    def __init__(self, num):
        if not isinstance(num, int):
            raise ValueError(
                'BNBlock must be initialized with an int value, but ' +
                '"num" value is of type: {}'.format(type(num))
            )
        elif num < 0 or num > 99999:
            raise ValueError(
                'BNBlock must be initialized with a value from 0 to 99999, ' +
                'but value was {}'.format(num)
            )
        self.value = num
        self.zero = True
    
    def adder(self, adder, balance):
        retval = 0
        self.value += adder.value
        self.value += balance
        if self.value > 99999:
            retval = int(self.value / 100000)
            self.value = self.value % 100000
        return retval
    
    def __str__(self):
        xstr = ''
        if self.zero:
            for i in (10, 100, 1000, 10000):
                if self.value < i:
                    xstr = xstr + '0'
        xstr = xstr + str(self.value)
        return xstr



class BigNumber:
    def __init__(self, xstr):
        self.data = []
        while len(xstr) >= 5:
            self.data.insert(0, BNBlock(int(xstr[(len(xstr)-5):])))
            xstr = xstr[:-5]
        if len(xstr) > 0:
            self.data.insert(0, BNBlock(int(xstr)))
    
    def __str__(self):
        for i in range(0, len(self.data)):
            if i == 0:
                xdata = self.data[0]
                xdata.zero = False
                xstr = str(xdata)
                xdata.zero = True
            else:
                xstr = xstr + str(self.data[i])
        return xstr
    
    def __add__(self, other):
        if isinstance(other, int):
            other = BigNumber(str(other))
        balance = 0
        value = BigNumber(str(self))
        for i in range(-1, -1 * (len(other.data) +1), -1):
            try:
                balance = value.data[i].adder(other.data[i], balance)
            except IndexError:
                value.data.insert(0, other.data[i])
                balance = value.data[i].adder(BNBlock(0), balance)
        index = -1 * len(other.data)
        while balance > 0:
            index = index -1
            try:
                balance = value.data[index].adder(BNBlock(0), balance)
            except IndexError:
                value.data.insert(0, BNBlock(balance))
                balance = 0
        return value
    
    __radd__ = __add__



# ------------------------------------------------------------------------



def main():
    
    with open('euler013.src', 'r', encoding='utf-8') as fi:
        data = fi.read().split('\n')
    
    
    # testing 'data' I see that it will add a 101th empty element, so I will 
    # remove it (<50 since every number in list should be 50-digit number)
    while len(data[-1]) < 50:
        data.pop()
    
    numbers = [BigNumber(x) for x in data]
    result = sum(numbers)
    result = str(result)
    print(result[:10])



if __name__ == "__main__":
    main()

