'''
@author：noc
@time：2020年3月29日
@url：https://leetcode-cn.com/problems/as-far-from-land-as-possible/
'''
'''
题解：用BFS求解最长路径。我们将陆地的节点加入队列中，每次出队时，检查这个队列的上下左右是否是海洋，如果是海洋的话，就把海洋的节点加入到队列中，
为了防止重复入队，就把海洋的节点标记成-1，当然还要值得注意的是，因为我们要计算路径到海洋的最长路径，队列保存的是第一层，而后面加入的节点是加入到
第一层的队列中。所以用p来保存每一层的队列。因为计算到最后肯定是空队列，但是这儿路径任然会加一，所以我们设置路径的初始值为-1。
时间复杂度：O（N^2） N是路径节点
空间复杂度：O（N^2）
'''
class Solution:
    def maxDistance(self, grid):
        lands = [[i, j] for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1]
        if len(lands) == 0 or len(lands) == len(grid) * len(grid[0]): return -1
        ret = -1
        while lands:
            p = lands
            lands = []
            while p:
                land = p.pop(0)
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if land[0] + x < 0 or land[0] + x == len(grid) or land[1] + y < 0 or land[1] + y == len(grid[0]) or grid[land[0] + x][land[1] + y] != 0:
                        continue
                    else:
                        grid[land[0] + x][land[1] + y] = -1
                        lands.append([land[0] + x, land[1] + y])
            ret += 1
        return ret

if __name__ == '__main__':
    grid = [[1,0,1],[0,0,0],[1,0,1]]
    out = Solution().maxDistance(grid)
    print(out)