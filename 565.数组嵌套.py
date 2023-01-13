#
# @lc app=leetcode.cn id=565 lang=python3
#
# [565] 数组嵌套
#

# @lc code=start
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            cnt = 0
            while nums[i] != -1:
                num = nums[i]
                cnt += 1
                nums[i] = -1
                i = num
            if ans < cnt:
                ans = cnt
        return ans
# @lc code=end

