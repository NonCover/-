'''
@author：noc
@time：2020年3月15日
@url：https://leetcode-cn.com/problems/max-area-of-island/
'''
'''
利用dfs求解,注释的代码是第一次通过的代码，运行的是调优后的代码
首先遍历二维数组，当然遍历到岛屿时，讲这个岛屿加入到队列中，并且置为0
然后出队，去看这个岛屿周围是否有岛屿，为1则是有岛屿，然后在把周围是岛屿的坐标入队
当检查过这个岛屿时，一定要将岛屿置为0
'''
class Solution(object):
    def maxAreaOfIsland(self, grid):
        # 给数组外面在加一层防止溢出
        for i in grid:
            i.insert(0, 0)
            i.append(0)
        grid.insert(0, [0] * len(grid[0]))
        grid.append([0] * len(grid[0]))
        print(grid)
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    queue = [(i, j)]
                    area = 1    # 保存当前在岛屿的面积
                    while queue:
                        x, y = queue.pop(0) # 出队
                        for move in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                            if grid[x + move[0]][y + move[1]] == 1:
                                area += 1
                                grid[x + move[0]][y + move[1]] = 0  # 查看过岛屿的话，就把这个岛屿变为0
                                queue.append((x + move[0], y + move[1]))    # 入队
                    ret = max(ret, area)    # 更新最大岛屿面积
        return ret


        # visted = set()  # 查看过的岛屿没必要在查看
        # max_area = 0    # 当前最大岛屿面积
        # is_1_grid = []
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             is_1_grid.append((i, j))
        # move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # for i, j in is_1_grid:
        #     if (i, j) not in visted:
        #         visted.add((i, j))
        #         queue = []
        #         queue.append((i, j))
        #         area = 1
        #         while queue:
        #             grid_x, grid_y = queue.pop(0)       # 弹出队列
        #             for m1, m2 in move: # 进行上下左右查看
        #                 if grid[grid_x + m1][grid_y + m2] == 1 and (grid_x + m1, grid_y + m2) not in visted:
        #                     area += 1   # 是岛屿的话加1
        #                     visted.add((grid_x + m1, grid_y + m2))  # 加入查看过的岛屿中
        #                     queue.append((grid_x + m1, grid_y + m2))    # 入队
        #         max_area = max(max_area, area)  # 更新最大岛屿面积
        # return max_area


if __name__ == '__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]



    out = Solution().maxAreaOfIsland(grid)
    print(out)
