class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict={}
        for s in strs:
            sS=''.join(sorted(s))
            if sS in anagramDict:
                anaList=anagramDict[sS]
                anaList.append(s)
                anagramDict[sS]=anaList
            else:
                anagramDict[sS]=[s]
        resList=[]
        for sublist in anagramDict.values():
            resList.append(sublist)
        return resList        