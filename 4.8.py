ds=input('nhap chuoi: ').split()
max=len(ds[0])
tam=ds[0]
for i in range(0, len(ds)):
    if len(ds[i]) > max:
        max=len(ds[i])
        tam=ds[i]
print(tam)