#
# @lc app=leetcode.cn id=2044 lang=python3
#
# [2044] 统计按位或能得到最大值的子集数目
#

# @lc code=start
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (1 << n)
        maxS = 0
        for mask in range(1 << n):
            for i in range(n):
                if mask & (1 << i):
                    dp[mask] = dp[mask ^ (1 << i)] | nums[i]
                    maxS = max(maxS, dp[mask])
        ans = 0
        for num in dp:
            if num == maxS:
                ans += 1
        return ans
            
# @lc code=end
solution = Solution()
nums = [3,2,1,5]
nums = [2,2,2]
print(solution.countMaxOrSubsets(nums))
