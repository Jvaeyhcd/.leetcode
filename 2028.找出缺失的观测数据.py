#
# @lc app=leetcode.cn id=2028 lang=python3
#
# [2028] 找出缺失的观测数据
#

# @lc code=start
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        _sum = sum(rolls)
        m = len(rolls)
        remain = (m + n) * mean - _sum
        if remain < n or remain > 6 * n:
            return []
        average = int(remain // n)
        ans = [average for _ in range(n)]
        remain -= average * n
        print(remain)
        for i in range(n):
            if remain > 6 - average:
                ans[i] = 6
                remain -= (6 - average)
            else:
                ans[i] += remain
                remain = 0
                break
        return ans
# @lc code=end

solution = Solution()
rolls = [1,5,6] 
mean = 3
n = 4

rolls = [1,2,3,4]
mean = 6
n = 4

rolls = [3,2,4,3]
mean = 4
n = 2

rolls = [4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5]
mean = 4
n = 40
print(solution.missingRolls(rolls, mean, n))