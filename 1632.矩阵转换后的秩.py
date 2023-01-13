#
# @lc app=leetcode.cn id=1632 lang=python3
#
# [1632] 矩阵转换后的秩
#

# @lc code=start
import collections
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
    
    
    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        uf = UnionFind(m * n)

        for r in range(m):
            table = collections.defaultdict(list)
            for c in range(n):
                table[matrix[r][c]].append(r * n + c)
            for _, arr in table.items():
                for i in range(len(arr) - 1):
                    uf.union(arr[i], arr[i + 1])
        
        for c in range(n):
            table = collections.defaultdict(list)
            for r in range(m):
                table[matrix[r][c]].append(r * n + c)
            for _, arr in table.items():
                for i in range(len(arr) - 1):
                    uf.union(arr[i], arr[i + 1])

        graph = collections.defaultdict(list)
        indeg = [0 for _ in range(m * n)]

        for r in range(m):
            arr = []
            for c in range(n):
                arr.append((matrix[r][c], r * n + c))
            arr.sort()
            for i in range(len(arr) - 1):
                if arr[i][0] != arr[i + 1][0]:
                    u = uf.find(arr[i][1])
                    v = uf.find(arr[i + 1][1])
                    graph[u].append(v)
                    indeg[v] += 1


        for c in range(n):
            arr = []
            for r in range(m):
                arr.append((matrix[r][c], r * n + c))
            arr.sort()
            for i in range(len(arr) - 1):
                if arr[i][0] != arr[i + 1][0]:
                    u = uf.find(arr[i][1])
                    v = uf.find(arr[i + 1][1])
                    graph[u].append(v)
                    indeg[v] += 1

        queue = collections.deque(i for i in range(m * n) if indeg[i] == 0 and uf.find(i) == i)
        
        rank = [1 for _ in range(m * n)]
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                rank[v] = max(rank[v], rank[u] + 1)
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)

        ans = [[1 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                ans[r][c] = rank[uf.find(r * n + c)]
        
        return ans

# @lc code=end

solution = Solution()
# input = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
# input = [[7,3,6],[1,4,5],[9,8,4]]
input = [[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]]
ans = solution.matrixRankTransform(input)
print(ans)