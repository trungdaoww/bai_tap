# đào văn trung
# mssv 1755251030100048
# import theo cau truc module.functionname
import mymath

values = [2,4,6,8,10]
print('Binh phuong : ')
for v in values:
    print(mymath.binhphuong(v))
print('Lap phuong: ')
for v in values:
    print(mymath.lapphuong(v))

print('Trung binh: ' + str(mymath.trbinh(values)))
