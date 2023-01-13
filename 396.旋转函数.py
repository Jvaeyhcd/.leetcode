#
# @lc app=leetcode.cn id=396 lang=python3
#
# [396] 旋转函数
#

# @lc code=start
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        f0 = 0
        for i, num in enumerate(nums):
            pre[i + 1] = pre[i] + num
            f0 += i * num
        ans = -0xf3f3f3f3
        for i in range(n):
            left = pre[n - i]
            right = pre[n] - pre[n - i]
            ans = max(ans, f0 + left * i - right * (n - i))
        return ans
# @lc code=end

solution = Solution()
nums = [4,3,2,6]
print(solution.maxRotateFunction(nums))