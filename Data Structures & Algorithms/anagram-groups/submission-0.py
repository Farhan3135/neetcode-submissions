class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        byComposition = defaultdict(list)

        for s in strs:
            composition = {}
            for l in s:
                letterOcc = composition.get(l,0)
                composition[l] = letterOcc + 1
            byComposition[frozenset(composition.items())].append(s)
        final = []
        for k,v in byComposition.items():
            final.append(v)
        return final