#
# @lc app=leetcode.cn id=2127 lang=python3
#
# [2127] 参加会议的最多员工数
#

# @lc code=start
from typing import List
from collections import deque

# 拓扑排序+基环森林树
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indeg = [0] * n
        for i in range(n):
            indeg[favorite[i]] += 1
        
        used = [False for _ in range(n)]
        # f[i]表示到节点i结束的最长游走路劲经过的节点个数
        f = [1] * n
        q = deque(i for i in range(n) if indeg[i] == 0)

        while q:
            u = q.popleft()
            used[u] = True
            v = favorite[u]
            f[v] = max(f[v], f[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
        
        ring = total = 0
        for i in range(n):
            if not used[i]:
                j = favorite[i]
                # 环的大小为2
                if favorite[j] == i:
                    total += (f[i] + f[j])
                    used[i] = used[j] = True
                # 环的大小大于2
                else:
                    u, cnt = i, 0
                    while True:
                        cnt += 1
                        u = favorite[u]
                        used[u] = True
                        if u == i:
                            break
                    ring = max(ring, cnt)
        return max(ring, total)


        
# @lc code=end

