#Chuong trinh dem so dong trong tep van ban
mo = open('trung.txt','r')
dong = 0
for c in mo:
    for i in range(0,len(c)):
        if c[i] == '\n':
            dong = dong+1
print("so dong la",dong)
