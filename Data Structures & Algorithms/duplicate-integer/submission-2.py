class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        sett = set()
        for n in nums:
            if n in sett:
                return True
            else:
                sett.add(n)

        return False