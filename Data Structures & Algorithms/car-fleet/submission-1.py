class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            t = (position[i], (target - position[i])/speed[i])
            stack.append(t)
        
        stack = sorted(stack, key = lambda x : x[0])

        carfleets = 0
        
        while stack:
            carfleets+=1
            timeMin = stack[-1][1]
            while len(stack) and stack[-1][1]<= timeMin:
                stack.pop()
        
        return carfleets
            
        
        
            