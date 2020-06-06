"""
author: noc
time: 2020年6月5日
url: https://leetcode-cn.com/problems/spiral-matrix/
"""

"""
用四个指针top，boutom，left，right，分别指向这个矩阵的上下左右的位置。我们按照顺时针遍历矩阵，就从 
    top位置：left > right
    right位置：top > bottom
    bottom位置：right > left
    left位置：bottom > top
如此往复，直到结束，注意一些边界问题，我会在注释中标明
"""

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        if m == 0: return ans
        n = len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1): ans.append(matrix[top][i])
            top += 1
            if len(ans) == m * n: break
            for i in range(top, bottom + 1): ans.append(matrix[i][right])
            right -= 1
            if len(ans) == m * n: break
            for i in range(right, left - 1, - 1): ans.append(matrix[bottom][i])
            bottom -= 1
            if len(ans) == m * n: break
            for i in range(bottom, top - 1, -1): ans.append(matrix[i][left])
            left += 1
            if len(ans) == m * n: break
        return ans

if __name__ == '__main__':
    input = [
             [ 1, 2, 3 ],
             # [ 4, 5, 6 ],
             # [ 7, 8, 9 ]
            ]
    out = Solution().spiralOrder(input)
    print(out)