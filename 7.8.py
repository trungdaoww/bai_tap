#Viet noi dung danh sach vao tep
def dua(ds,tep):
    mo = open(tep,'a+')
    mo.write(ds)
    
#thu kiem tra
ds = 'ABC'
dua(ds,'trung.txt')
mo = open('trung.txt','r')
print(mo.read())
mo.close()
