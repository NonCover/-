'''
author: noc
time: 2020年4月10日
url: https://leetcode-cn.com/problems/sudoku-solver/
'''
'''
递归每一种可能性，当前的值无法满足条件的时候就回溯，修改之前的值，直到每一个值符合条件的时候就返回True。
当我插入board[i][j]的值时，前提要求这个位置为空，我们依次插入["1","2","3","4","5","6","7","8","9"]，如果某一个值成立的话，就填下一个空，
当下一个空，无论填哪一个值都无法满足条件，就说明我们即将回溯到之前的空修改，修改后依然无法满足，那就继续回溯，直到满足条件
由于数据量是固定的，所以计算机最对会计算 9！的9次方这么多次，因为上一个空填入的值会影响下一个。
'''
class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.recur(board)

    def recur(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for val in ["1","2","3","4","5","6","7","8","9"]:
                        if self.row_col_constraint(i, j, board, val):
                            board[i][j] = val
                            if self.recur(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    # 行, 列约束
    def row_col_constraint(self, row, col, board, val):
        for i in range(9):
            if board[row][i] == val:
                return False

        for i in range(row - row % 3, row - row % 3 + 3):
            for j in range(col - col % 3, col - col % 3 + 3):
                if board[i][j] == val:
                    return False

        for i in range(9):
            if board[i][col] == val:
                return False
        return True

if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(board)
    for b in board:
        print(b)