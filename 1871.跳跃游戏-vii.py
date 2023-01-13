#
# @lc app=leetcode.cn id=1871 lang=python3
#
# [1871] 跳跃游戏 VII
#

# @lc code=start
import collections


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        arr = list(s)
        n = len(arr)
        q = collections.deque()
        q.append(0)
        visited = [False for _ in range(n)]
        visited[0] = True
        while q:
            u = q.popleft()
            if u == n - 1:
                return True
            for i in range(minJump, maxJump + 1):
                v = u + i
                if v >= n:
                    break
                if arr[v] == '0' and not visited[v]:
                    q.append(v)
                    visited[v] = True
        return False
# @lc code=end

solution = Solution()
s = "011010"
minJump = 2
maxJump = 3
print(solution.canReach(s, minJump, maxJump))