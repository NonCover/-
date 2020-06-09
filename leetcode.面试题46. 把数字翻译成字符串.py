"""
author: noc
time: 2020年6月9日
url: https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
"""

"""
解法：类似力扣55题：跳跃游戏，理解了此题这题手到擒来，所以此题解法为动态规划，当然利用回溯法也能求解，但复杂度较高，这里用DP最好。
首先，我们通过数字来推理出字符串，如果我们从左到右来推理的话，我们求余运算不好求，所以我们从右到左。也就是从低向上求解。
num = x1x2x3... xi
dp[i] = 表示从最后一个字符到 xi 所组成的字符个数
我们需要注意的是 如果 xi-1xi 不能组成字母的话，dp[i] = dp[i + 1]，只能继承上一个
如果能够组成的话，dp[i] = dp[i + 1] + dp[i + 2]  
"""

class Solution:
    def translateNum(self, num: int) -> int:
        N = len(str(num)) + 1
        dp = [0] * N

        ## 初始状态
        dp[N - 1], dp[N - 2] = 1, 1   ## dp[-1] = xi 组成的字符，dp[-2] = xi-1xi组成的字符
        y = num % 10    ## xi
        num //= 10
        x= num % 10     ## xi-1

        ## 从低向上
        for i in range(N - 3, -1, -1):
            temp = x * 10 + y
            dp[i] = dp[i + 1] + dp[i + 2] if temp >= 10 and temp <= 25 else dp[i + 1]   ## 状态转移
            num //= 10
            y = x
            x = num % 10
        return dp[0]

    """
    注意发现没有，我们的dp之与当前状态的后两个状态有关，所以我们优化数组
    """
    def optimize(self, num: int) -> int:
        y = num % 10
        num //= 10
        x = num % 10

        a, b = 1, 1     ## a = dp[i + 1]    b = dp[i + 2]
        while num:
            tmp = x * 10 + y
            c = a + b if tmp >= 10 and tmp <= 25 else a     ## c = dp[i]

            ## 继续向左取余计算
            y = num % 10
            num //= 10
            x = num % 10

            ## 更新 a b
            b = a
            a = c
        return a

if __name__ == '__main__':
    num = 26
    out = Solution().translateNum(num)
    print(out)