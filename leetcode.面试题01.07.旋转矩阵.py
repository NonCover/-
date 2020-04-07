'''
@author:noc
@time:2020年4月7日
@url:https://leetcode-cn.com/problems/rotate-matrix-lcci/
'''
'''
这是一道来自微软的面试题
题解：先水平，在对角线交换后，即可得到90度旋转后的矩阵。找到矩阵其中的规律即可
时间复杂度：O（N^2）
空间复杂度：O（1）  除去保存矩阵的matrix数组
'''
class Solution:
    def rotate(self, matrix):
        N = len(matrix)
        for i in range(N // 2):
            # 矩阵的水平交换
            matrix[i], matrix[N - i - 1] = matrix[N - i - 1], matrix[i]
        for i in range(N - 1):
            for j in range(N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        pass

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    print(matrix)
