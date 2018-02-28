class BigNumber:
    def __init__(self):
        self.xstr = ""
        # 13 cifre
        self.xbuffer = None
    
    def nextval(self):
        if self.xbuffer is None:
            tmp_buffer = self.xstr[0:13]
            self.xstr = self.xstr[:-13]
            self.xbuffer = []
            for ch in tmp_buffer:
                self.xbuffer.append(int(ch))
            return self._nv()
        else:
            self.xbuffer = self.xbuffer[1:]
            self.xbuffer.append(int(self.xstr[0]))
            self.xstr = self.xstr[1:]
            return self._nv()
    
    def _nv(self):
        value = 1
        for i in self.xbuffer:
            value = value * i
        return value
    
    def hasnext(self):
        return len(self.xstr) >= 13



big = BigNumber()



with open('euler008.src', 'r', encoding='utf-8') as fi:
    for xline in fi:
        xline = xline.strip('\r\n')
        big.xstr = big.xstr + xline



result = 0



while big.hasnext():
    value = big.nextval()
    if value > result:
        result = value


print(result)
