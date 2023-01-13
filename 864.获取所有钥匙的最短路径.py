#
# @lc app=leetcode.cn id=864 lang=python3
#
# [864] 获取所有钥匙的最短路径
#

# @lc code=start
from curses.ascii import isalpha, islower, isupper
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        keys = set([chr(ord('a') + i) for i in range(26)])
        m, n = len(grid), len(grid[0])
        total_keys = 0
        q = []
        vis = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    q = [(i, j, 0, 0)]
                    vis.add((i, j, 0))
                elif grid[i][j].islower():
                    total_keys += 1
        
        while q:
            i, j, step, status = q.pop(0)
            if bin(status).count("1") == total_keys:
                return step
            
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if not (0 <= ni < m and 0 <= nj < n) or (ni, nj, status) in vis:
                    continue
                if grid[ni][nj] == '#':
                    continue
                elif grid[ni][nj].islower():
                    vis.add((ni, nj, status | (1 << (ord(grid[ni][nj]) - ord('a')))))
                    q.append((ni, nj, step + 1, status | (1 << (ord(grid[ni][nj]) - ord('a')))))
                    continue
                elif grid[ni][nj].isupper() and (1 << (ord(grid[ni][nj]) - ord('A'))) & status == 0:
                    continue
                
                vis.add((ni, nj, status))
                q.append((ni, nj, step + 1, status))

        return -1
# @lc code=end

