from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        @lru_cache(None)
        def dp(day):
            if day >= len(days):
                return 0                      # was: return curCost

            day7 = len(days)
            day30 = len(days)
            for i in range(day + 1, len(days)):
                if days[i] >= days[day] + 7:
                    day7 = i
                    break
            for i in range(day + 1, len(days)):
                if days[i] >= days[day] + 30:
                    day30 = i
                    break

            return min(
                costs[0] + dp(day + 1),       # cost moved from the argument
                costs[1] + dp(day7),          # to the return side
                costs[2] + dp(day30),
            )

        return dp(0)