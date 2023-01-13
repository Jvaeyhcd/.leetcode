#
# @lc app=leetcode.cn id=2104 lang=python3
#
# [2104] 子数组范围和
#

# @lc code=start
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        min_left, max_left = [0] * n, [0] * n
        min_stack, max_stack = [], []
        for i in range(n):
            num = nums[i]
            while min_stack and num < nums[min_stack[-1]]:
                min_stack.pop()
            min_left[i] = min_stack[-1] if min_stack else -1
            min_stack.append(i)

            while max_stack and num >= nums[max_stack[-1]]:
                max_stack.pop()
            max_left[i] = max_stack[-1] if max_stack else -1
            max_stack.append(i)
        
        min_right, max_right = [0] * n, [0] * n
        min_stack, max_stack = [], []
        for i in range(n - 1, -1, -1):
            num = nums[i]
            while min_stack and num < nums[min_stack[-1]]:
                min_stack.pop()
            min_right[i] = min_stack[-1] if min_stack else n
            min_stack.append(i)

            while max_stack and num >= nums[max_stack[-1]]:
                max_stack.pop()
            max_right[i] = max_stack[-1] if max_stack else n
            max_stack.append(i)

        ans = 0
        for i, num in enumerate(nums):
            max_ = (max_right[i] - i) * (i - max_left[i]) * num
            min_ = (min_right[i] - i) * (i - min_left[i]) * num
            ans += (max_ - min_)
        return ans
# @lc code=end

