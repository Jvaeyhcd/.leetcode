#
# @lc app=leetcode.cn id=753 lang=python3
#
# [753] 破解保险箱
#

# @lc code=start
from collections import deque


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        ans = ''
        dq = deque(['0' * n])
        used = set(['0' * n])
        ans = '0' * n
        while dq:
            pw = dq.popleft()
            for i in range(k - 1, -1, -1):
                npw = pw[1:] + str(i)
                if npw in used: continue
                dq.append(npw)
                used.add(npw)
                ans += str(i)
                break
        return ans
# @lc code=end

solution = Solution()
n = 4
k = 10
ans = solution.crackSafe(n, k)
print(ans)