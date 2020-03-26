'''
@author：noc
@time：2020年3月26日
@url；https://leetcode-cn.com/problems/available-captures-for-rook/
'''
'''
题解：
先找到白车在棋盘中的位置，然后在依次上下 左右的移动的去找白棋吃。
时间复杂度：O（N^2） 主要是找到白车需要N*N的复杂度的时间，
空间复杂度：O（1）
'''
class  Solution:
    def numRookCaptures(self, board):
        ret = 0
        r1 = -1
        r2 = -1
        # 找出白棋
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r1 = i
                    r2 = j
        move = [1, -1];
        ## 北南方向去吃棋
        for m in move:
            x = r1;
            y = r2;
            while (board[x][y] != 'B'):
                x += m
                if (x < 0 or x == 8): break
                elif (board[x][y] == '.'): continue
                elif (board[x][y] == 'p'):
                    ret += 1
                    break
        # 东西
        for m in move:
            x = r1;
            y = r2;
            while board[x][y] != 'B':
                y += m;
                if (y < 0 or y == 8): break
                elif (board[x][y] == '.'): continue
                elif (board[x][y] == 'p'):
                    ret += 1
                    break
        return ret

if __name__ == '__main__':
    board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    out = Solution().numRookCaptures(board)
    print(out)