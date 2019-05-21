#đào văn trung
#th2.8: tìm tổng số chẵn trong dãy fibonacci nhỏ hơn 4000.000
a,b=1,2
total=0
print(a,end=" ")
while (a<=4000000-1):
    if a%2==0:
        total += a
    a,b=b,a+b
    print(a,end=" ")
print("tổng số chẵn trong dạy",total)