tienthuc=0
while True:
    s = input('Nhập nhật ký giao dịch: ')
    if not s:
        break
    giatri = s.split(' ')
    kihieu = giatri[0]
    sotien = int(giatri[1])
    if kihieu == 'D':
        tienthuc+= sotien
    elif kihieu == 'W' :
        tienthuc-= sotien
    else:
        pass
print ('So tien hien co trong tk: ',tienthuc)