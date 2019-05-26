class chunhat:
    def __init__(self,dai,rong):
        self.d = dai
        self.r = rong
    def dt(self):
        return self.d*self.r

cn = chunhat(3,4)
print(cn.dt())
