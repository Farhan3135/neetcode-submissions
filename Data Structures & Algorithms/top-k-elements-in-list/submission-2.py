class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numOcc = {}

        for n in nums:
            occ = numOcc.get(n,0)
            numOcc[n] = occ+1
        
        occNum = defaultdict(list)
        for num, occ in numOcc.items():
            occNum[occ].append(num)
        
        final = []
        runningOcc = len(nums)
        while k:
            numberList = occNum.get(runningOcc,[])
            if numberList:
                k-= len(numberList)
                final += numberList
            runningOcc -=1
        
        return final

