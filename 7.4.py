# Chuong trinh doc n dong dau tien cua tep
def filedong(ten,dong):
    from itertools import islice
    with open(ten) as f:
        for line in islice(f, dong):
            print(line)
filedong('trung.txt',2)
