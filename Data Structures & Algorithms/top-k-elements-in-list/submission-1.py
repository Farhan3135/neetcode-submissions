class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numToOcc = {}
        for i in nums:
            occ =numToOcc.get(i,0)
            numToOcc[i] = occ+1
        
        # occ to num
        occToNum = defaultdict(set)
        for key,v in numToOcc.items():
            occToNum[v].add(key)
    
        # till len(final) != k keep going backward form len(nums) and adding to keep O(n)
        maxOcc = len(nums)
        final = []

        print(occToNum)
        
        while k != 0:
            frequent = occToNum.get(maxOcc,None)
            
            if frequent is not None:
                print(f"k is {k}")
                k-= len(frequent)
                final = final + list(frequent)
            maxOcc-=1
        
        return final

    