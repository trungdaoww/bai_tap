import math
a = float(input("Nhap vao a : "))
b = float(input("Nhap vao b : "))
c = float(input("Nhap vao c : "))
d = b**2-4*a*c;
if d<0:
    print("Phuong trinh vo nghiem")
elif d==0 :
    print("Phuong trinh co nghiem kep ",-b/(2*a))
else :
    x1 = (-b - math.sqrt(d))/(2*a)
    x2 = (-b + math.sqrt(d))/(2*a)
    print("Phuong trinh co hai nghiem : ","x1= ",x1,",","x2= ",x2)