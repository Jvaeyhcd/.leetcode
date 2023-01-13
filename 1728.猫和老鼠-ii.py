#
# @lc app=leetcode.cn id=1728 lang=python3
#
# [1728] 猫和老鼠 II
#

import sys
 
sys.setrecursionlimit(1000000)

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        m_pos, c_pos, f_pos = None, None, None
        for i in range(m):
            for j in range(n):
                pos = [i, j]
                ch = grid[i][j]
                if ch == 'M':
                    m_pos = pos
                elif ch == 'C':
                    c_pos = pos
                elif ch == 'F':
                    f_pos = pos
        
        @lru_cache(None)
        def dfs(t: int, mouse_x: int, mouse_y: int, cat_x: int, cat_y: int) -> bool:
            if t > 1000 or (mouse_x == cat_x and mouse_y == cat_y) or (cat_x == f_pos[0] and cat_y == f_pos[1]):
                return False
            if mouse_x == f_pos[0] and mouse_y == f_pos[1]:
                return True

            cat_turn = t % 2 == 1
            pos, jump = [mouse_x, mouse_y], mouseJump
            if cat_turn:
                pos, jump = [cat_x, cat_y], catJump

            for dx, dy in dirs:
                for jp in range(jump + 1):
                    nx, ny = pos[0] + dx * jp, pos[1] + dy * jp
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] == '#':
                        break
                    if not cat_turn and dfs(t + 1, nx, ny, cat_x, cat_y):
                        return True
                    elif cat_turn and not dfs(t + 1, mouse_x, mouse_y, nx, ny):
                        return False
            
            return cat_turn
        
        return dfs(0, m_pos[0], m_pos[1], c_pos[0], c_pos[1])

# @lc code=end

solution = Solution()
grid = ["####F","#C...","M...."]
catJump = 1
mouseJump = 2

# grid = [".M...","..#..","#..#.","C#.#.","...#F"]
# catJump = 3
# mouseJump = 1

print(solution.canMouseWin(grid, catJump, mouseJump))