class Bitset:

    def __init__(self, size: int):
        self.bits=[0 for i in range(size)]
        self.flipbits=[1 for i in range(size)]
        self.count1=0
        self.count0=size
        self.size=size
        
    def fix(self, idx: int) -> None:
        if self.bits[idx]!=1:
            self.bits[idx]=1
            self.count1+=1
            self.count0-=1
            self.flipbits[idx]=0
        
    def unfix(self, idx: int) -> None:
        if self.bits[idx]!=0:
            self.bits[idx]=0
            self.count0+=1
            self.count1-=1
            self.flipbits[idx]=1
    def flip(self) -> None:
        self.count0,self.count1=self.count1,self.count0
        self.bits,self.flipbits=self.flipbits,self.bits
    def all(self) -> bool:
        return  self.count1==self.size
    def one(self) -> bool:
        return self.count1>0
    def count(self) -> int:
        return self.count1
    def toString(self) -> str:
        return "".join(map(str,self.bits))
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()