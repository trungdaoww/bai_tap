import math;
x1 = int(input(" Nhap x1 : "))
y1 = int(input("Nhap y1 : "))
x2 = int(input(" Nhap x2 : "))
y2 = int(input("Nhap y2 : "))
d1 = (x2-x1)^2;
d2 = (y2-y1)^2;
res = math.sqrt(d1+d2)
print(" khoang cach hai diem la : ",res)