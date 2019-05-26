# đào văn trung
# mssv 1755251030100048
import Sequential_Search as ham
n = int(input("Nhap vao so nguyen duong n: "))
ls = []
for i in range(0,n):
    x = int(input("Nhap phan tu thu %s : "%(i)))
    ls.append(x)
item = int(input("Nhap vao phan tu can tim kiem : "))
ham.Sequential_Search(ls,item)
            
            
        
