n=int(input('nhap n: '))
l=[]
a,b=0,1
while b<n:
    a,b=b,a+b
    l.append(a)
print(l)