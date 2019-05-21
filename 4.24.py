s=input('nhap cau: ')
H,T=0,0
for i in s:
    if i.isupper():
        H+=1
    if i.islower():
        T+=1
print(H)
print(T)