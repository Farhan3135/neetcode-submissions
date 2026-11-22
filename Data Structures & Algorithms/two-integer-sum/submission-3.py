class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nset={}
        for i, n in enumerate(nums):
            diff = target- n
            if diff in nset:
                return [nset[diff], i]
            else:
                nset[n] = i
        return []