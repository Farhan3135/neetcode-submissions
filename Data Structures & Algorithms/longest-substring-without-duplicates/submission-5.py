class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        letterSet = set()
        ans = 0
        start = 0
        for end in range(len(s)):
            while s[end] in letterSet:
                letterSet.remove(s[start])
                start+=1
            letterSet.add(s[end])
            ans = max(ans, end-start+1)
        return ans

