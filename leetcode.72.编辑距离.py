'''
@author:noc
@time:2020年4月6日
@url:https://leetcode-cn.com/problems/edit-distance/
'''

class Solution:
    def minDistance(self, word1, word2):
        # 自底向上
        _N1 = len(word1)
        _N2 = len(word2)
        # 保存每一步的结果数组
        # dp = [[0] * (_N2 + 1) for _ in range(_N1 + 1)]
        # dp[0] = [i for i in range(_N2 + 1)] # dp[0][i] 保存的是当word1为空时，需要转换得到word2的做小步骤
        # for i in range(_N1 + 1):
        #     dp[i][0] = i    # dp[i][0] 保存的是 当 word2为空时，word1转换到word2的最小步骤，也就是依次删除word1的每一个字符
        #
        # for i in range(1, _N1 + 1):
        #     for j in range(1, _N2 + 1):
        #         if word1[i - 1] == word2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] # 什么操作都不做
        #         else:
        #             dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1    # 依次是替换，删除，插入操作
        # return dp[_N1][_N2]
        # 自顶向上  递归
        import functools
        @functools.lru_cache(None)  # 缓存
        def helper(i, j):
            if _N1 == i or _N2 == j:
                return _N1 - i + _N2 - j    #
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1) # 啥都不自哦
            else:
                inserted = helper(i, j + 1) # 插入
                replaced = helper(i + 1, j + 1) # 替换
                deleted = helper(i + 1, j) # 删除
            return min(inserted, replaced, deleted) + 1


        return helper(0, 0)
if __name__ == '__main__':
    word1 = 'horse'
    word2 = 'ros'
    out = Solution().minDistance(word1, word2)
    print(out)