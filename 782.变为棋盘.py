#
# @lc app=leetcode.cn id=782 lang=python3
#
# [782] 变为棋盘
#

# @lc code=start
from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)

        row_mask = col_mask = 0
        for i in range(n):
            row_mask |= board[0][i] << i
            col_mask |= board[i][0] << i
        
        reverse_row_mask = ((1 << n) - 1) ^ row_mask
        reverse_col_mask = ((1 << n) - 1) ^ col_mask
        row_cnt = col_cnt = 0

        for i in range(n):
            cur_row_mask = cur_col_mask = 0
            for j in range(n):
                cur_row_mask |= board[i][j] << j
                cur_col_mask |= board[j][i] << j

            if cur_row_mask != row_mask and cur_row_mask != reverse_row_mask or cur_col_mask != col_mask and cur_col_mask != reverse_col_mask:
                return -1
            
            row_cnt += cur_row_mask == row_mask
            col_cnt += cur_col_mask == col_mask

        
        def get_moves(mask:  int, count: int) -> int:
            ones = mask.bit_count()
            if n & 1:
                if abs(n - 2 * ones) != 1 or abs(n - 2 * count) != 1:
                    return -1
                if ones == n // 2:
                    return n // 2 - (mask & 0xAAAAAAAA).bit_count()
                else:
                    return (n + 1) // 2 - (mask & 0x55555555).bit_count()
            else:
                if ones != n // 2 or count != n // 2:
                    return -1
                count1 = n // 2 - (mask & 0xAAAAAAAA).bit_count()
                count2 = n // 2 - (mask & 0x55555555).bit_count()
                return min(count1, count2)
        
        row_moves = get_moves(row_mask, row_cnt)
        col_moves = get_moves(col_mask, col_cnt)
        return -1 if row_moves == -1 or col_moves == -1 else row_moves + col_moves
# @lc code=end

