class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        multiDict= defaultdict(list)
        answer=[]
        for string in strs:
            sortString=''.join(sorted(string))
            multiDict[sortString].append(string)
        print(multiDict)
        for key in multiDict.keys():
            answer.append(multiDict[key])
        return answer

        






        