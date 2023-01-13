#
# @lc app=leetcode.cn id=675 lang=python3
#
# [675] 为高尔夫比赛砍树
#

# @lc code=start
import collections
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        trees = sorted((v, r, c) for r, row in enumerate(forest) for c, v in enumerate(row) if v > 1)
        m, n = len(forest), len(forest[0])
        ans = x = y = 0
        for _, tx, ty in trees:
            d = self.dist(forest, x, y, tx, ty)
            # print(tx, ty, d)
            if d < 0:
                return -1
            ans += d
            x, y = tx, ty
        return ans

    def dist(self, forest: List[List[int]], x: int, y: int, tx: int, ty: int) -> int:
        m, n = len(forest), len(forest[0])
        queue = collections.deque()
        queue.append([x, y, 0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[x][y] = True
        while queue:
            x, y, d = queue.popleft()
            if tx == x and ty == y:
                return d
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and forest[nx][ny] > 0:
                    queue.append([nx, ny, d + 1])
                    visited[nx][ny] = True
        return -1
# @lc code=end

s = Solution()
forest = [[1,2,3],[0,0,4],[7,6,5]]
forest = [[1,2,3],[0,0,0],[7,6,5]]
forest = [[2,3,4],[0,0,5],[9,8,6]]
print(s.cutOffTree(forest))