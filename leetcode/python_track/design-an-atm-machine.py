class ATM:

    def __init__(self):
        self.atm=[0,0,0,0,0]
        self.notes=[20,50,100,200,500]
    
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.atm[i]+=banknotesCount[i]
    def withdraw(self, amount: int) -> List[int]:
        j=4
        ans=[0]*5
        while j>=0 and amount:
            ans[j] = min(self.atm[j], amount//self.notes[j])
            
            amount -= ans[j]*self.notes[j]
            j -= 1
             
        if amount:
            return [-1]
        else:
            for k, money in enumerate(self.atm):
                self.atm[k] = money - ans[k]
            return ans


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)