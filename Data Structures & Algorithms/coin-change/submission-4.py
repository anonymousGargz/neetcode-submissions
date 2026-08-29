class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amountDict={}

        def recurseCC( i, curAmount):
            if (i<0 and curAmount==0):
                return 0
            if (i<0):
                return 100000000000000
            if curAmount in amountDict:
                return amountDict[curAmount]
            ansI=847385783
            if curAmount>= coins[i]:
                ansI=min(1+recurseCC(i, curAmount-coins[i]), 1+recurseCC(i-1, curAmount-coins[i]), recurseCC(i-1, curAmount))
            else:
                ansI=min(1+recurseCC(i-1, curAmount-coins[i]), recurseCC(i-1, curAmount))
            amountDict[curAmount]=ansI
            return ansI
        ans=recurseCC(len(coins)-1, amount)
        if ans==100000000000000:
            return -1
        else:
            return ans
            
