#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = nums[0]
        ans = nums[0]
        for i in range(1, n):
            dp[i][1] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            dp[i][0] = min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            if dp[i][1] > ans:
                ans = dp[i][1]
            
        return ans
# @lc code=end
solution = Solution()
nums = [2,3,-2,4]
nums = [1,2,3,4,5,-9,-2,21,3]
nums = [1,2,3,4,5,-6,-5]
print(solution.maxProduct(nums))
