class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set()
        for n in nums:
            nSet.add(n)
        
        maxCount = 0
        for num in nums:
            
            if num-1 not in nSet:
                number = num
                count = 0
                while number in nSet:
                    count += 1
                    number +=1
                else:
                    maxCount = max(count, maxCount)
            
        
        return maxCount
                        