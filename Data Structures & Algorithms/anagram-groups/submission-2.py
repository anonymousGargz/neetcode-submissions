class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict=defaultdict(list)
        for s in strs:
            counterObj= ''.join(sorted(s))
            anagramDict[counterObj].append(s)
        return list(anagramDict.values())
