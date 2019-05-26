# Doc mot file, tinh so ki tu, so tu, so dong
k = open("trung.txt","r")
char,wc,lc=0,0,0
for line in k:
    for i in range(0,len(line)):
        char +=1
        if(line[i]==' '):
            wc += 1
        if (line[i]=='\n'):
            wc, lc=wc+1,lc+1
print("so ki tu hien thi : %d\nso tu : %d\nso dong : %d"%(char,wc,lc))
