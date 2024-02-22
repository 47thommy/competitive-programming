class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >len(num):
            return "0"
        monotonic_stack=[]
        for i in range(len(num)):
            while k and len(monotonic_stack)>0 and monotonic_stack[-1]>num[i]:
                k-=1
                monotonic_stack.pop()
            monotonic_stack.append(num[i])
        if k:
            monotonic_stack=monotonic_stack[:len(monotonic_stack)-k]
        return"".join(monotonic_stack).lstrip('0') or '0'