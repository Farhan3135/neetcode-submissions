class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        lMax = height[left]
        rMax = height[right]
        maxWater = 0

        while left<right:
            if height[left]<=height[right]:
                maxWater+=(lMax - height[left])
                left+=1
                lMax = max(lMax, height[left])

            elif height[left]>height[right]:
                maxWater+=rMax - height[right]
                right-=1
                rMax = max(rMax, height[right])
        return maxWater

