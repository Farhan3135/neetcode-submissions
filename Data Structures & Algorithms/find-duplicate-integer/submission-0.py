class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        p3 = 0

        while slow != p3:
            slow = nums[slow]
            p3 = nums[p3]
        
        return p3
        