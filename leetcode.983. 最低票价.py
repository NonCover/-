"""
author: noc
time: 2020年5月6日
url: https://leetcode-cn.com/problems/minimum-cost-for-tickets/
"""
from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        ## dp[i] = 第i天 到 第days[-1]天 所需要的最便宜票价
        dp = [0 for _ in range(0, days[-1] + 31)]
        d = N - 1
        for i in range(days[-1], days[0] - 1, -1):
            ## 第i天需要出行旅行
            if days[d] == i:
                ## 状态转移方程
                """
                dp[i + 7] + costs[1] = 只需要购买出行七天的购票方式，所以要加上后第7天的钱。
                costs[1] 只会影响到 第i天到第i + 6天
                以此类推。。。
                """
                dp[i] = min(dp[i + 1] + costs[0], dp[i + 7] + costs[1], dp[i + 30] + costs[2])
                d -= 1
            else:
                """
                当前天数不出行的话，直接等于后一天的
                """
                dp[i] = dp[i + 1]
        return dp[days[0]]

if __name__ == '__main__':
    days = [1,4,6,7,8,20]
    costs = [2, 7, 15]
    out = Solution().mincostTickets(days, costs)
    print(out)