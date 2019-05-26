# đào văn trung
# mssv 1755251030100048
#Su dung module maxmin.py
import maxmin
#Tim phan tu lon nhat va nho nhat
n = int(input("Nhap vao so luong trong danh sach : "))
if n<=0:
    print("So vua nhap khong hop le")
else:
    lst = []
    for i in range(0,n):
        x = int(input("Nhap vao phan tu thu %s : "%(i)))
        lst.append(x)
print("Phan tu lan nhat trong danh sach la: ",maxmin.lonnhat(lst))
print("Phan tu nho nhat trong danh sach la: ",maxmin.nhonhat(lst))

