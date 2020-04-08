'''
@author:noc
@time:2020年4月8日
@url:https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
'''
'''
BFS遍历，我们使用队列来存要走的方格位置，当方格位置为1时，我们就跳过，因为一开始我们就将不满足条件的位置值设为1.
'''
class Solution:
    def movingCount(self, m, n, k):
        ret = 0
        if k == 0: return 1
        check = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                val = i % 10 + i // 10 + j % 10 + j // 10
                if val > k:
                    check[i][j] = 1
        movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 移动方式
        # 队列
        queue = [(0, 0)]
        while queue:
            X, Y = queue.pop(0)
            for move in movement:
                a, b = X + move[0], Y + move[1]
                if a < 0 or a == m or b < 0 or b == n or check[a][b] == 1:  # 如果为 1 则可能是 走过的方格或者 不符合小于等于 k 条件
                    continue
                check[a][b] = 1
                queue.append((X + move[0], Y + move[1]))
                ret += 1
        return ret

if __name__ == '__main__':
    m, n = 28, 15
    k = 9
    out = Solution().movingCount(m, n, k)
    print(out)

