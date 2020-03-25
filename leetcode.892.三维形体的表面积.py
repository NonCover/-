'''
@author: noc
@time: 2020年3月25日
@url: https://leetcode-cn.com/classic/problems/surface-area-of-3d-shapes
'''

'''
题解：总的来说，一开始题目的描述不清楚，在理解题意上花了点时间，不过这题还是简单的，
grid[i][j] * 4 - 2 代表当前重叠起来的正方体表面积，由于如果周围存在其他正方体的话，他们相交的部分是不会算入表面积中，所以我们要 减去上面和左边相交的面积，
grid[i][j] * 4 - 2 - min(grid[i][j], grid[i - 1][j]) * 2 +  min(grid[i][j], grid[i][j - 1]) * 2，当然我们总是检查上面和左面，防止重复减去相同的面。
为了防止溢出问题，还需要判断当前各自是否处于边缘，由于我们只需要检查上面和左边的面积，所以只需判断当前正方体是否在第一排或者第一列。
时间复杂度：O（N*N）N代表grid的行列数
空间复杂度：O（1）
'''
class Solution:
    def surfaceArea(self, grid):
        # N = [[0] * 50] * 50
        ret = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         N[i][j] = grid[i][j]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: continue
                elif i == 0 and j == 0:
                    ret += (grid[i][j] * 4 + 2)
                elif i == 0:
                    ret += (grid[i][j] * 4 + 2 - min(grid[i][j], grid[i][j - 1]) * 2)
                elif j == 0:
                    ret += (grid[i][j] * 4 + 2 - min(grid[i][j], grid[i - 1][j]) * 2)
                else:
                    ret += (grid[i][j] * 4 + 2 - min(grid[i][j], grid[i - 1][j]) * 2 - min(grid[i][j], grid[i][j - 1]) * 2)
        return ret

if __name__ == '__main__':
    grid = [[2,2,2],[2,1,2],[2,2,2]]
    out = Solution().surfaceArea(grid)
    print(out)