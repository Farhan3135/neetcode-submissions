class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        maxLen = 0
        numsSet  = set(nums)
        for n in nums: 
            if n-1 not in numsSet:
                
                runningLen = 0
                num = n
                while num in numsSet:
                    runningLen +=1
                    num+=1
                maxLen = max(maxLen, runningLen)
        
        return maxLen