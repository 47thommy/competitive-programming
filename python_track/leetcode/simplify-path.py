class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        current=""
        res=""
        for  p in path+"/":
            if p == "/":
                if(current==".."):
                    if stack:
                        stack.pop()
                elif(current != "." and current !=""):
                    stack.append(current)
                current=""
            else:
                current=current+p
        if len(stack)==0:
            return "/"
        for p in stack:
            res=res+"/"+p
        return res
                
            
        