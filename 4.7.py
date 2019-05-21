s=input('nhập chuỗi: ')
l=[]
for i in s:
    if i.isnumeric() :
        continue
    l.append(i)
h=' '.join(l)
print(l)
print(h)