class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l<r:
            diff = target-numbers[l]
            
            while numbers[r]>diff:
                r-=1
            if numbers[r] == diff:
                return [l+1, r+1]
            l+=1
        
        return None
