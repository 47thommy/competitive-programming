class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                subStr=""
                while stack[-1]!="[":
                    subStr=stack.pop()+subStr
                stack.pop()
                nums=""
                
                while stack and "0"<=stack[-1]<="9":
                    nums=stack.pop()+nums
                num=int(nums)
                stack.append(num*subStr)
        return "".join(stack)