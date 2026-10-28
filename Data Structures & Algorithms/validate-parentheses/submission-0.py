class Solution:
    def isValid(self, s: str) -> bool:
        bracketsMap = {'{': '}', '(': ')', '[':']'}
        openStack = []
        for b in s:
            if b in bracketsMap:
                openStack.append(b)
            else:
                if not openStack:
                    return False
                ans = openStack.pop()
                if b != bracketsMap[ans]:
                    return False
        return True and not len(openStack)
