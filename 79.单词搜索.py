#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
# dfs
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(x, y, pos, visited):
            if pos == len(word) - 1:
                return True
            
            visited[x][y] = True
            for nx, ny in [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]:
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[pos + 1] and not visited[nx][ny]:
                    if dfs(nx, ny, pos + 1, visited):
                        return True
            visited[x][y] = False
            return False
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    visited[r][c] = True
                    if dfs(r, c, 0, visited): return True
        
        return False


# @lc code=end

