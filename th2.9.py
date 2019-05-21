#đào văn trung
#th2.9 viết chương trinh đếm số kí tự trong 1 xâu nhập từ bàn phím, lưu các kí tự vào cấu trúc từ điển
str=input('nhập vào')
dict={}
for i in str:
    dict[i] = str.count(i)
print(dict)