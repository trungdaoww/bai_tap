#Chuyen doi mot so La Ma thanh so nguyen
class lama_nguyen:
    def __init__(self,s):
        self.s = s
    
    def chuyen(self):
        rom_val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        int_val = 0
        def kiemtra(self):
            for i in self.s:
                if i not in rom_val:
                    print("So vua nhap khong hop le")
                    break
                
        for i in range(len(self.s)):
            if i>0 and rom_val[s[i]]>rom_val[s[i-1]]:
                int_val += rom_val[s[i]] - 2*rom_val[s[i-1]]
            else:
                int_val += rom_val[s[i-1]]
            return int_val
### kiem tra
s = input("Nhap vao day La Ma : ")
print(lama_nguyen(s).chuyen())

            
    
        
