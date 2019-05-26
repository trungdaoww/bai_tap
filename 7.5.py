#noi van ban vao tep va hien thi
def file_name(ten):
    from itertools import islice
    with open(ten,'a') as file:
        file.write("Day la them vao")
    mo = open(ten)
    print(mo.read())
file_name("trung.txt")
