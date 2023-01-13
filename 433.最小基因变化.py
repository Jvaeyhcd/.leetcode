#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
import collections
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        def nextDNA(s: str) -> List[str]:
            dna = ["A", "C", "G", "T"]
            arr = []
            for i, ch in enumerate(s):
                for c in dna:
                    if c != ch:
                        nxt = s[:i] + c + s[i+1:]
                        arr.append(nxt)
            return arr
        
        visited = collections.defaultdict(lambda:0)
        visited[start] = 1
        queue = [(start, 0)]
        while queue:
            for _ in range(len(queue)):
                u, step = queue.pop(0)
                if u == end:
                    return step
                for v in nextDNA(u):
                    if not visited[v] and v in bank:
                        visited[v] = 1
                        queue.append((v, step + 1))
        return -1
# @lc code=end

