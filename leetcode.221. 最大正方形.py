"""
author: noc
time: 2020年5月8日
url: https://leetcode-cn.com/problems/maximal-square/
"""
"""
dp解法三步骤：
1. 状态：dp[i][j] 表示 （i， j）代表某正方形的右下角的最长边长
2. 重叠子问题,dp[i][j] 表示的正方形周长与其上方，左上，右方相关。
3. 状态转移方程: 
    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    当 i 或 j 为 0 时，dp[i][j] = 1
    
再来看，我们发现dp[i][j] 只与 上、左、左上相关，我们可以优化dp为一维空间
"""
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        height = len(matrix)
        width = len(matrix[0])
        maxL = 0
        # dp = [[0] * width for _ in range(height)]
        dp = [0] * (width)
        for i in range(height):
            nw = 0  ## 每次遍历每行时，需要把左上重置为 0
            for j in range(width):
                if matrix[i][j] == "1":
                    ## 保存的是 左上边长
                    nextNw = dp[j]
                    if i == 0 or j == 0:
                        ## 在矩阵上左边缘的话，正方形周长只能为1
                        # dp[i][j] = 1
                        dp[j] = 1
                    else:
                        ## 状态转移方程
                        # dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                        dp[j] = min(dp[j], dp[j - 1], nw) + 1
                    nw = nextNw
                    maxL = max(maxL, dp[j])
                else:
                    ## 注意当前不为1时，需要设置为0
                    dp[j] = 0
        return maxL * maxL

if __name__ == '__main__':
    matrix = [["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]
    out = Solution().maximalSquare(matrix)
    print(out)