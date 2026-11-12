class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        monoStack = []
        maxArea = 0
        
        for i,h in enumerate(heights):
            if not monoStack or monoStack[-1][0]<=h:
                monoStack.append((h,i))
                continue
            
            while monoStack and monoStack[-1][0]>h:
                oldH, oldI = monoStack.pop()
                width = i-oldI
                maxArea = max(maxArea, (i-oldI)*oldH)
                lowestI = oldI
            else:
                monoStack.append((h,oldI))
        
        
        while monoStack:
            h,i = monoStack.pop()
            maxArea = max((len(heights)-i)*h, maxArea)

        return maxArea
