#Class hinh tron
class Circle:
    def __init__(self,bankinh):
        self.r = bankinh
    def chuvi(self):
        return self.r*2*3.14
    def dientich(self):
        return self.r**2*3.14
## kiem tra
hinhtr = Circle(4)
print("Chu vi la %s ,dien tich la %s "%(hinhtr.chuvi(),hinhtr.dientich()))
        
