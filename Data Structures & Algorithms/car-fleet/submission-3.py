class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [(position[i], (target - position[i])/speed[i]) for i in range(len(position))]
        cars = sorted(cars)
        stack = []
        for pos, time in cars:            
            while stack and stack[-1][1] <= time:
                stack.pop()
            else:
                stack.append((pos, time))
        
        return len(stack)

