from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        myDict = Counter(s)
        finalS = ""
        for i in range(0, len(order)):
            if (order[i] in myDict):
                finalS += order[i] * myDict[order[i]]
                del myDict[order[i]]
        for char in myDict:
            finalS += char * myDict[char]
        return finalS

        