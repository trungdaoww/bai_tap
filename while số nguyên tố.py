# tim tat ca cac so nguyen to tu 0 den 100 dùng vòng lặp while
i = 2
while i< 100:
    j = 2
    while j <= i//j :
        if i%j == 0 :
            break
        j = j+1
    else :
        print(i)
    i= i+1

