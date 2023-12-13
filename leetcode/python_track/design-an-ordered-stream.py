class OrderedStream:

    def __init__(self, n: int):
        self.arr = [""] * n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1] = value
        ans = []
        if self.pointer == idKey - 1:
            while self.pointer < len(self.arr) and self.arr[self.pointer] != "":
                ans.append(self.arr[self.pointer])
                self.pointer += 1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)