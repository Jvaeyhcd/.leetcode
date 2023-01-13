#
# @lc app=leetcode.cn id=1388 lang=python3
#
# [1388] 3n 块披萨
#

# @lc code=start
from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        t = len(slices) // 3
        return max(self.rob(slices[1:], t), self.rob(slices[:-1], t))

    def rob(self, nums: List[int], cnt: int) -> int:
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        dp = [[0 for _ in range(cnt + 1)] for _ in range(n)]
        dp[0][1] = nums[0]
        dp[1][1] = max(nums[0], nums[1])
        for i in range(2, n):
            for t in range(1, cnt + 1):
                dp[i][t] = max(dp[i - 1][t], dp[i - 2][t - 1] + nums[i])
        return dp[n - 1][cnt]
# @lc code=end
solution = Solution()
slices = [8,9,8,6,1,1]
# slices = [1,2,3,4,5,6]
slices = [4,1,2,5,8,3,1,9,7]
# slices = [3,1,2]
slices = [3,5,4,4,6,6,3,4,4,7,10,5,7,2,2]
print(solution.maxSizeSlices(slices))
