# đào văn trung
# mssv 1755251030100048
# Tim kiem nhi phan
import nhiphan
n = int(input("Nhap so luong phan tu: "))
if n<= 0:
    print("So vua nhap khong hop le .")
else:
    lst = []
    for i in range(0,n):
        x = int(input("Phan tu thu %s la : "%(i)))
        lst.append(x)
    val = int(input("Nhap vao gia tri can tim : "))
    sap = lst[:].sort(reverse = False)
    print(sap)
    #nhiphan.binary_search(sap,val)
   
    
