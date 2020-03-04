# @author: noc
# @time: 2020年3月4日13点33分
# @url: https://leetcode-cn.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid):
        time = 0    # 计时
        # 将腐烂的橘子入队：
        rot = [[i, j] for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2]
        # 设置一个集合用来保存新鲜的橘子
        fresh = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1}
        # 存放新鲜的橘子被污染后的坐标:
        end = set()
        # 在网格外层在加一层, 方式溢出错误
        for i in grid:
            i.insert(0, 0)
            i.append(0)
        grid.insert(0, [0 for _ in range(len(grid[0]))])
        grid.append([0 for _ in range(len(grid[0]))])
        # 腐烂的橘子只能让上下左右的新鲜橘子腐烂:
        move = [(0, 1), (0, -1), (-1, 0), (1, 0)]   # 上下左右
        while fresh:
            if len(rot) == 0:   # 判断是否还存在新的腐烂橘子
                return -1
            next_rot = []
            for curr_rot in rot:
                curr_x, curr_y = curr_rot   # 当前腐烂橘子的坐标
                for x, y in move:
                    dx, dy = curr_x + x, curr_y + y # dx，dy代表腐烂橘子周围的橘子坐标
                    if (dx, dy) in fresh and (dx, dy) not in end:
                        end.add((dx, dy))   # 新鲜的橘子被腐烂后加入这个集合
                        fresh.remove((dx, dy))  # 该橘子已腐烂，从fresh中剔除
                        next_rot.append([dx, dy])
            time += 1
            rot = next_rot
        if fresh == None:
            return -1
        return time

if __name__ == "__main__":
    out = Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
    print(out)

