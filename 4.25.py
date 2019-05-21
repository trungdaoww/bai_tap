s=input('nhap danh sach: ').split(',')
l=[]
for i in s:
    if int(i) % 2!= 0:
        l.append(i)
print(l)