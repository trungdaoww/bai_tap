n=range(1,1000000)
l=[]
for i in n:
    nt=1
    for j in range(2,i-1):
        if i%j==0:
            nt=0
    if nt==1:
        l.append(i)
print(tuple(l))