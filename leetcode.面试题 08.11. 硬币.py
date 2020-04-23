'''
author: noc
time: 2020年4月23日
url: https://leetcode-cn.com/problems/coin-lcci/
'''
'''
这题其实就是完全背包的问题，给了我们可以无限使用的硬币，我们使用这些硬币来组合成总额为n，那么有多少种组合方式。照样用dp来求解此类问题，因为有重叠子问题。
dp[i] 代表当前金额为i时有多少种组成情况。
状态转移方程 dp[i] = dp[i] + dp[i - coin] 
'''
class Solution:
    def waysToChange(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1   # base case
        coins = [25, 10, 5, 1]
        for coin in coins:
            for i in range(coin, n + 1):
                dp[i] += dp[i - coin]
            print(dp)
        return dp[-1]

if __name__ == '__main__':
    n = 10
    out = Solution().waysToChange(n)
    print(out)