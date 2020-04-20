'''
author: noc
time: 2020年4月20日
url: https://leetcode-cn.com/problems/number-of-islands/
'''
from typing import List

'''
经典BFS，套用基本BFS模板即可
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    queue = []
                    ans += 1
                    queue.append((i, j))
                    grid[i][j] = "0"
                    while queue:
                        x, y = queue.pop(0)
                        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                                queue.append((nx, ny))
                                grid[nx][ny] = "0"  # 标记成访问

        return ans
if __name__ == '__main__':
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","1"],
            ["0","0","0","1","0"]]
    out = Solution().numIslands(grid)
    print(out)