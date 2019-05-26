#Class chap nhan mot chuoi va in chuoi
class IOstring:
    def __init__(self):
        self.ch = ""
    def get_string(self):
        self.ch = input("Nhap vao mot chuoi : ")
    def print_string(self):
        print(self.ch.upper())
## kiem tra
chay = IOstring()
chay.get_string()
chay.print_string()
