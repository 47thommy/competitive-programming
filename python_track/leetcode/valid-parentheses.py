class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        check={")":"(", "}":"{","]":"["}
        for i in range(len(s)):
            if s[i] == "(" or s[i]=="[" or s[i]=="{":
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if check[s[i]]!=top:
                    return False
        if len(stack)>0:
            return False
        return True
        