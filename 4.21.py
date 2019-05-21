giatri = []
nhap= input('Nhập các số nhị phân: ').split(',')
for p in nhap:
    intp = int(p, 2)
    if intp % 5==0:
        giatri.append(p)
print (','.join(giatri))