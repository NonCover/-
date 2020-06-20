"""
author: noc
time: 2020年6月20日
url: https://leetcode-cn.com/problems/regular-expression-matching/
"""

"""
解法：
    动态规划：
        1. 状态：dp[i][j] = s[0, i) 与 p[0, j) 是否匹配
        2. 状态基：dp[0][0] = True 两个空字符串肯定是匹配的
        3. 状态转移方程：
            由于是 p 字符串来匹配 s 字符串，肯定是从 p 字符串入手，分成以下情况
            1. p[j - 1]为字母或者 ’.‘ 时
                我们判断 s[i - 1] 是否与 p[j - 1] 相等，是的话， dp[i][j] = dp[i - 1][j - 1]
                否的话， dp[i][j] = True
            2. 当p[j - 1] 为 "*" 时
                此时需要注意的是， p[j - 1] 为 "*" 匹配的是 p[j - 2] 任意个字符包括 0 个，
                所以我们需要用 p[j - 2] 去与 s[i - 1] 进行比较，如果两个字符相等的话，
                我们 dp[i][j] = dp[i - 1][j] or dp[i][j - 2], 此时 "*" 代表的就是正整数了，那么 ”*“ 个 p[j - 2]字符与 s 匹配的话没相当于将 s[i - 1] 从 s 中 removal,
                此时我们就要看 dp[i - 1][j] 是否匹配了
                不过不等的话，说明此时的 "*" 代表的为 0，不用去与 s 字符串中的任意字符进行匹配，所以有 dp[i][j] = dp[i][j - 2]
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        dp = [[False for _ in range(lp + 1)] for _ in range(ls + 1)]
        dp[0][0] = True     ## base case
        for i in range(ls + 1):
            for j in range(1, lp + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if self.mach(s, p, i, j - 1):   ## 判读s[i - 1] 是否与 p[j - 2] 相等
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    if self.mach(s, p, i, j):
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]


    def mach(self, s: str, p: str, i: int, j: int) -> bool:
        if i == 0: return False
        if p[j - 1] == '.': return True
        return s[i - 1] == p[j - 1]


if __name__ == '__main__':
    s = "mississippi"
    p = "mis*is*p*."
    out = Solution().isMatch(s, p)
    print(out)