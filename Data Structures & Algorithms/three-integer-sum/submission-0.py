class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        triplets = set()

        for top in range(len(nums)):
            target = -1*nums[top]

            l = top+1
            r = len(nums)-1
            while l<r:
                diff = target - nums[l]
                while r>l and nums[r]>diff:
                    r-=1
                if nums[r] == diff and r != l:
                    triplets.add((nums[top],nums[l],nums[r]))
                l+=1
        final = []
        
        for t in triplets:
            final.append(list(t))
        
        return list(triplets)
            
