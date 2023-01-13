#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#

# @lc code=start
import collections
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        graph = collections.defaultdict(list)
        indeg = [0 for _ in range(m * n)]

        for i in range(m):
            for j in range(n):
                for di, dj in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < m and 0 <= jj < n and matrix[ii][jj] > matrix[i][j]:
                        u, v = j + n * i, jj + n * ii
                        graph[u].append(v)
                        indeg[v] += 1
        
        queue = collections.deque(i for i in range(m * n) if indeg[i] == 0)
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                u = queue.popleft()
                for v in graph[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        queue.append(v)
        return ans

# @lc code=end

