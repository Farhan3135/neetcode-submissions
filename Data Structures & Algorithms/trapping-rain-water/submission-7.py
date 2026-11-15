class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        lmax = height[l]
        rmax = height[r]
        maxWater = 0
        while l<r:

            while l<r and height[l] <= height[r]:
                water = min(rmax,lmax)-height[l]

                if water<0:
                    water = 0
                
                maxWater += water

                l+=1
                lmax = max(lmax,height[l])
            
            while l<r and height[l] > height[r]:
                water = min(rmax,lmax)-height[r]
                
                if water<0:
                    water = 0

                maxWater += water


                r-=1
                rmax = max(rmax,height[r])
            
        return maxWater