# đào văn trung
# mssv 1755251030100048
import numpy as ny
data_type = [('ten','S15'),('lop',int),('ccao',float)]
students = [('James',5,48.5),('Nail',6,52.5),('Paul',5,42.1),('Pit',5,40.11)]
#Tao cau truc mang
st = ny.array(students,dtype=data_type)
print(st)
print("Sap xep :")
print(ny.sort(ny.sort(st,order = 'lop'),order = 'ccao'))
