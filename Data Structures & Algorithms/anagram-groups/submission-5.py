class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict=defaultdict(list)
        for s in strs:
       
            ss=str(sorted(s))
            myDict[ss].append(s)
        ans=[]
        for key, vals in myDict.items():
            ans.append(vals)
        return ans
