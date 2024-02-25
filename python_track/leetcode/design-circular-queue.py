class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=[None]*k
        self.k=k
        self.remove=0
        self.add=0
        self.size=0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue[self.add]=value
            self.size+=1
            self.add=(self.add+1)%self.k
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.remove]=None
            self.size-=1
            self.remove=(self.remove+1)%self.k
            return True

    def Front(self) -> int:
        if self.isEmpty():return -1
        return self.queue[self.remove]
    def Rear(self) -> int:
        if self.isEmpty():return -1
        return self.queue[self.add-1]
    def isEmpty(self) -> bool:
        return True if self.size==0 else False
    def isFull(self) -> bool:
        return True if self.size==self.k else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()