class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr=[]
        for i in range(len(s)):
            arr.append(s[i])
        for i in range(0,len(s),2*k):
            arr[i:k+i]=arr[i:k+i][::-1]
        return "".join(arr)
            