'''
author: noc
time: 2020年4月15日
url: https://leetcode-cn.com/problems/01-matrix/
'''
'''
自动忽略本人的垃圾代码，这题以前做过类似的，所以今天的打卡很简答，但无奈本人的代码实在可读性太差，参考的官方的解答，发下本质思想不变，主要是利用超级源点做BFS遍历。
我的做法是遍历每一个 1节点，初始矩阵只有 1 和 0，然后做BFS遍历每一个1节点的下一层有不有 0节点，如果有返回距离，没得的话，将下一层的所有节点做超级源点，继续遍历
超级源点的下一层。直到找到0。
时间复杂度：O（rows * cols）

官方BFS解答：将所有 O 节点做超级源点，做广搜时，我们把下一层节点 + 上一层远点 + 1这样下一层的节点到最近的 0 的距离就出来了，然后把下一层节点入队。
继续周而复始的循环，直到队列为空。 和leetcode1162题目一模一样，换了一种问的方式而已
'''
class Solution:
    def updateMatrix(self, matrix):
        rows = len(matrix)  # 行
        cols = len(matrix[0]) # 列
        # moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == 0: continue
        #         queue = [(i , j)]
        #         distance = 0
        #         visted = set()
        #         while True:
        #             distance += 1
        #             q = []  # 存放当前层对应得下一层位置
        #             while queue:
        #                 row, col = queue.pop(0)
        #                 for x, y in moves:
        #                     if row + x < 0 or row + x == rows or col + y < 0 or col + y == cols: # 防止溢出
        #                         continue
        #                     if (row + x, col + y) in visted: # 防止无限循环
        #                         continue
        #                     q.append((row + x, col + y))
        #                     visted.add((row + x, col + y))
        #             for x, y in q:
        #                 if matrix[x][y] == 0:   # 当前层如果有0的话，说明matrix[i][j] 最近的0就是当前递归层数
        #                     matrix[i][j] = distance
        #                     queue = []
        #                     q = []
        #                     break
        #             if q == []: break
        #             queue = q
        #         # print(matrix)
        # return matrix

        # 超级源点
        # 将所有得0当成一个超级源点
        queue = [(i , j) for i in range(rows) for j in range(cols) if matrix[i][j] == 0]
        visted = set(queue)
        while queue:
            i, j = queue.pop(0)
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visted:
                    matrix[ni][nj] = matrix[i][j] + 1
                    queue.append((ni, nj))
                    visted.add((ni, nj))
        return matrix

if __name__ == '__main__':
    matrix = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
    out = Solution().updateMatrix(matrix)
    print(out)