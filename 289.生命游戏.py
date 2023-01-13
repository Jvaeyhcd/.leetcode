#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        m, n = len(board), len(board[0])
        for row in range(m):
            for col in range(n):
                cnt = 0
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]
                    if 0 <= r < m and 0 <= c < n and abs(board[r][c]) == 1:
                        cnt += 1
                if board[row][col] == 1 and (cnt < 2 or cnt > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and cnt == 3:
                    board[row][col] = 2

        
        for row in range(m):
            for col in range(n):
                if board[row][col] > 0:
                    board[row][col] = 1
                elif board[row][col] < 0:
                    board[row][col] = 0
# @lc code=end

