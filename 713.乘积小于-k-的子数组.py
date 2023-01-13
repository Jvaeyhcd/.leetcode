#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans, cur, l, r = 0, 1, 0, 0
        while r < n:
            cur *= nums[r]
            while l < n and cur >= k:
                cur //= nums[l]
                l += 1
            ans += (r - l + 1)
            r += 1
        return ans
# @lc code=end

solution = Solution()
nums = [10,5,2,6]
k = 100

# nums = [1,2,3]
# k = 9
print(solution.numSubarrayProductLessThanK(nums, k))