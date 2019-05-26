#Sao chep noi dung cua tep nay sang tep khac
tep1 = open("trung.txt","r")
tep2 = open("trung2.txt","w")
doc = tep1.readline()
while doc:
    tep2.write(doc)
    doc = tep1.readline()
tep2 = open("trung2.txt","r")
print(tep2.read())
tep1.close()
tep2.close()
