#
# @lc app=leetcode.cn id=802 lang=python
#
# [802] 找到最终的安全状态
#

# @lc code=start
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        rev_graph = [[] for _ in graph]
        in_deg = [0] * n
        for i in range(n):
            for node in graph[i]:
                rev_graph[node].append(i)
            in_deg[i] = len(graph[i])
        
        que = collections.deque()
        for i in range(n):
            if in_deg[i] == 0:
                que.append(i)
        
        while que:
            u = que.popleft()
            for v in rev_graph[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    que.append(v)
        
        ans = []
        for i in range(n):
            if in_deg[i] == 0:
                ans.append(i)
        
        return ans



# @lc code=end

