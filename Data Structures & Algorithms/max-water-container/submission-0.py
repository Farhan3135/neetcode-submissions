class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights)-1
        maxArea = 0
        
        while r>l:
            length = min(heights[r],heights[l])
            newArea  = length*(r-l)
            print(newArea)
            maxArea = max(maxArea, newArea)
            
            if heights[r]<=heights[l]:
                heightR = heights[r]
                while r>l and heights[r]<=heightR:
                    r-=1
            else:
                heightL = heights[l]
                while l<r and heights[l]<=heightL:
                    l+=1
        return maxArea
