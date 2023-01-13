#
# @lc app=leetcode.cn id=1306 lang=python3
#
# [1306] 跳跃游戏 III
#

# @lc code=start
import collections
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = collections.deque()
        q.append(start)
        n = len(arr)
        visited = [False for _ in range(n)]
        visited[start] = True
        while q:
            u = q.popleft()
            if arr[u] == 0:
                return True
            v1 = u + arr[u]
            v2 = u - arr[u]
            if 0 <= v1 < n and not visited[v1]:
                q.append(v1)
                visited[v1] = True
            if 0 <= v2 < n and not visited[v2]:
                q.append(v2)
                visited[v2] = True

        return False
        
# @lc code=end

