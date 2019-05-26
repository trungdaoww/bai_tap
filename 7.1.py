# Doc file va in dao nguoc ket qua
input_file = open("trung.txt","r")
for line in input_file:
    l = len(line)
    s=''
    while (l>=1):
        s += line[l-1]
        l = l-1
    print(s)
input_file.close()
