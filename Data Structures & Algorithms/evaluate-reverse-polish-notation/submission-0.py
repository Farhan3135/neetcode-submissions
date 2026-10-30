class Solution:
    def calc(n1, n2, op:str):
        if op == "-":
            return n1 - n2
        elif op == "+":
            return n1 + n2
        elif op == "*":
            return n1 * n2
        elif op == "/":
            return n1 / n2
        
    def evalRPN(self, tokens: list[str]) -> int:



        stack = []
        operators = {"+","-","*","/"}

        for t in tokens: 
            if t not in operators:
                stack.append(t)
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                ans = Solution.calc(int(n1),int(n2),t)
                stack.append(ans)
        
        return int(stack[-1])
             