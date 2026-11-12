class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {'(': ')', '[':']', '{': '}'}
        stack = []
        for b in s:
            if b in bracketMap:
                stack.append(b)
            else:
                if not stack:
                    return False
                opp = stack.pop()
                if b != bracketMap[opp]:
                    return False
        
        return not stack and True


