#Doc n dong cuoi cung cua tep
import sys
import os
def tep(ten,sdong):
    bufsize = 8192
    fsize = os.stat(ten).st_size
    print(fsize)
    iter = 0
    with open(ten) as f:
        if bufsize > fsize:
            bufsize = fsize-1
            data = []
            while True:
                iter += 1
                f.seek(fsize-bufsize*iter)
                data.extend(f.readlines())
                if len(data) >= sdong or f.tell() == 0:
                    print(''.join(data[-sdong:]))
                    break
tep('trung.txt',2)

