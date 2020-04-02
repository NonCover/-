'''
@author:noc
@time:2020年4月2日
@url:https://leetcode-cn.com/problems/game-of-life/
'''
'''
题解：生命游戏是每一个programmer接触最多个最有趣的一个游戏。对于此题我们不需要什么高深莫测的语法，只需要找到规则，一步一步算出下一步的存亡状态。
时间复杂度：O（mn） m为一维数组长度 n为二维数组长度
空间复杂度：O（1）  增加 -1 和 2 两种状态避免空间冗余
'''
class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        L1, L2 = len(board[0]), len(board)
        move = [[1, 1], [1, -1], [-1, 1], [-1, -1], [-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(L2):
            for j in range(L1):
                amount = 0  # 周围活细胞的个数
                for m in move:
                    # m[0] m[1] 表示移动方式
                    if i + m[0] < 0 or i + m[0] == L2 or j + m[1] < 0 or j + m[1] == L1:
                        continue    # overflow
                    if abs(board[i + m[0]][j + m[1]]) == 1: # 统计活的细胞
                        amount += 1
                if amount == 3 and board[i][j] == 0:
                    board[i][j] = 2     # 过去是死的复活
                elif (amount > 3 or amount < 2) and board[i][j] == 1:
                    board[i][j] = -1    # 过去是活的死了
        # for i, j in dead:
        #     board[i][j] = 0
        # for i, j in life:
        #     board[i][j] = 1
        for i in range(L2):
            for j in range(L1):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0


if __name__ == '__main__':
    board = [
              [0,1,0],
              [0,0,1],
              [1,1,1],
              [0,0,0]
            ]
    Solution().gameOfLife(board)
    print(board)