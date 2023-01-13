#
# @lc app=leetcode.cn id=754 lang=python3
#
# [754] 到达终点数字
#

# @lc code=start
import collections


class Solution:
    def reachNumber(self, target: int) -> int:
        q = collections.deque()
        q.append((0, 0))
        while q:
            u, step = q.popleft()
            if u == target:
                return step
            step += 1
            for v in [u + step, u - step]:
                q.append((v, step))


# @lc code=end

