class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict = {}
        tDict = {}
        for l in s:
            n = sDict.get(l,0)+1
            sDict[l] = n
        for l in t:
            n = tDict.get(l,0) +1
            tDict[l] = n
        
        return tDict == sDict

