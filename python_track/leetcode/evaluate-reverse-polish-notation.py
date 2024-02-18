class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rcheck = {"+", "-", "/", "*"}
        stack = []
        res = int(tokens[0])
        for token in tokens:
            if stack and token in rcheck:
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if token == "+":
                    res = op2 + op1
                elif token == "-":
                    res = op2 - op1
                elif token == "/":
                    res = int(op2 / op1)  
                elif token == "*":
                    res = op2 * op1
                stack.append(res)
            else:
                stack.append(int(token))  
        return res
