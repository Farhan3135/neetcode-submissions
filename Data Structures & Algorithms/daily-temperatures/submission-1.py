class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final = [0 for i in range(len(temperatures))]
        stack = []
        for i, t in enumerate(temperatures):

            while stack and stack[-1][0]<t:
                lastT, lastI = stack.pop()
                final[lastI] = i-lastI
            
            stack .append((t,i))
        
        return final


            