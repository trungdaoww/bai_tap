s=input('nhap cau: ')
c,so=0,0
for i in s:
    if i.isalpha():
        c+=1
    if i.isnumeric():
        so+=1
print(c)
print(so)