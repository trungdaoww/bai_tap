class nguoi:
    def gioitinh(self):
        return "Chua biet"
class Nam(nguoi):
    def gioitinh(self):
        return "Nam"

class Nu(nguoi):
    def gioitinh(self):
        return "Nu"
anam = Nam()
anu = Nu()
print(anu.gioitinh())
print(anam.gioitinh())
