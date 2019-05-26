# đào văn trung
# mssv 1755251030100048
import numpy as np
data_type = [('name','S15'),('class',int),('height',float)]
students_details = [('James',5,48.5),('Nail',6,52.5),('Paul',5,42.10),('Pit',5,40.11)]
# Tao cau truc mang
students = np.array(students_details,dtype = data_type)
print("Mang goc: ")
print(students)
print(" Sap xep theo chieu cao :")
print(np.sort(students,order = "height"))
