#
# @lc app=leetcode.cn id=854 lang=python3
#
# [854] 相似度为 K 的字符串
#

# @lc code=start
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        a1, a2 = [], []
        for x, y in zip(s1, s2):
            if x != y:
                a1.append(x)
                a2.append(y)
        n = len(a1)
        if n == 0:
            return 0

        ans = n - 1
        def dfs(i: int, step: int):
            nonlocal ans
            if step > ans:
                return
            while i < n and a1[i] == a2[i]:
                i += 1
            if i == n:
                ans = min(ans, step)
                return
            
            d = sum(a1[j] != a2[j] for j in range(i, len(a1)))
            min_swap = (d + 1) // 2
            if step + min_swap >= ans:
                return
            
            for j in range(i + 1, n):
                if a1[j] == a2[i]:
                    a1[i], a1[j] = a1[j], a1[i]
                    dfs(i + 1, step + 1)
                    a1[i], a1[j] = a1[j], a1[i]
        
        dfs(0, 0)
        return ans
# @lc code=end

