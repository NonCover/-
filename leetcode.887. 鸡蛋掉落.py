'''
author: noc
time: 2020年4月11日
url: https://leetcode-cn.com/problems/super-egg-drop/submissions/
'''
'''
解释一下dp[k][m]的含义，保存的是用k个鸡蛋测试m次所能得出F值得楼层数。因为m永远不会大于楼层数，即使是线性测试也只能测试N次得出F值。
何时得出结论？只有当dp[k][m] > N时，我们就能够得出答案了。
'''
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # 二维数组优化成一维数组
        dp = [0] * (K + 1)
        ret = 0 # 扔的次数
        while dp[-1] < N:
            ret += 1
            pre = 0
            for k in range(1, K + 1):
                c = dp[k]   # 保存上一次dp[k]的值, 避免此次更新修改了值，造成结果错误
                dp[k] = pre + dp[k] + 1
                pre = c     # 更新
        return ret

        # dp = [[0] * (N + 1) for _ in range(K + 1)]
        # m = 0
        # k = 0
        # while dp[k][m] < N:
        #     m += 1
        #     for k in range(1, K + 1):
        #         dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1
        #         print(dp[k][m])
        # return m
if __name__ == '__main__':
    K = 100
    M = 10000
    out = Solution().superEggDrop(K, M)
    print(out)