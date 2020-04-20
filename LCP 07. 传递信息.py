'''
author: noc
time: 2020年4月18日
url: https://leetcode-cn.com/problems/chuan-di-xin-xi/
'''
from typing import List

class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        self.ans = 0
        size = len(relation)
        def dfs(idx, k, num):
            if k == 0:
                if num == n - 1:
                    self.ans += 1
                    return
                else:
                    return
            for i in range(size):
                if relation[i][0] == num:
                    dfs(i, k - 1, relation[i][1])

        for i in range(size):
            # 从0开始
            if relation[i][0] == 0:
                dfs(i, k - 1, relation[i][1])

        return self.ans

if __name__ == '__main__':
    n = 5
    relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]
    k = 3
    out = Solution().numWays(n, relation, k)
    print(out)