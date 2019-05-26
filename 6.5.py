# Class de dao chuoi tung chu
class daochuoi:
    def __init__(self,ch):
        self.chuoi = ch
    def dao(self):
        return ' '.join(reversed(self.chuoi.split()))
## kiem tra
st = 'hello py.'
thu = daochuoi(st)
print(thu.dao())
