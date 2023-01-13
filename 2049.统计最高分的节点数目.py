#
# @lc app=leetcode.cn id=2049 lang=python3
#
# [2049] 统计最高分的节点数目
#

# @lc code=start
import collections
from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        graph = collections.defaultdict(lambda:[])
        for i, num in enumerate(parents):
            if num != -1:
                graph[num].append(i)

        # 记录以某个节点为根的元素的个数
        self.cnts = collections.defaultdict(lambda:0)

        def dfs(u: int):
            if u in self.cnts:
                return self.cnts[u]
            ans = 1
            for v in graph[u]:
                ans += dfs(v)
            self.cnts[u] = ans
            return ans
        
        dfs(0)
        maxS, ans = 0, 0
        for u in range(n):
            cnt1 = self.cnts[0] - self.cnts[u]
            cnt2 = self.cnts[graph[u][0]] if len(graph[u]) > 0 else 0
            cnt3 = self.cnts[graph[u][1]] if len(graph[u]) > 1 else 0
            res = 1
            if cnt1 > 0: res *= cnt1
            if cnt2 > 0: res *= cnt2
            if cnt3 > 0: res *= cnt3
            if maxS < res:
                maxS = res
                ans = 1
            elif maxS == res:
                ans += 1
        
        return ans
# @lc code=end

solution = Solution()
parents = [-1,2,0,2,0]
# parents = [-1,2,0]
print(solution.countHighestScoreNodes(parents))