class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        final = [0 * i for  i in range(len(temperatures))]
        stack = []
        for i, t in enumerate(temperatures):

            if not len(stack):
                stack.append((t,i))
                continue
            
            last = stack[-1]
            
            while last[0] < t:
                final[last[1]] = i - last[1]
                stack.pop()
                
                if not len(stack):
                    break
                
                last = stack[-1]
            
            stack.append((t,i))
        
        return final
        
        

