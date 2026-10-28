class Solution:
    def trap(self, height: list[int]) -> int:
        leftTallest = [0 for i in range(len(height))]
        rightTallest = [0 for i in range(len(height))]
        
        maxSoFar = 0
        for i in range(len(height)):
            leftTallest[i] = maxSoFar
            maxSoFar = max(maxSoFar,height[i])

        maxSoFar = 0
        for i in range(len(height)-1,-1,-1):
            rightTallest[i] = maxSoFar
            maxSoFar = max(maxSoFar,height[i])

        totalWater = 0
        for i, h in enumerate(height):
            bottleNeck = min(leftTallest[i], rightTallest[i])
            print(bottleNeck)
            water = bottleNeck - h
            if water > 0:
                totalWater += water
        
        return totalWater