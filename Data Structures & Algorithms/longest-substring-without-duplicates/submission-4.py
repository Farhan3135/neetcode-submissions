class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sMap = {}
        start = 0
        end = 0
        ans = 0
        while end != len(s):
            val = sMap.get(s[end],None)
            
            if val is None:
                
                sMap[s[end]] = end
                ans = max(ans,end-start)
                end +=1
            else:
                while start != val+1:
                    sMap[s[start]] = None
                    start+=1
                start = val+1

        return ans +1 

