#
# @lc app=leetcode.cn id=910 lang=python
#
# [910] 最小差值 II
#

# @lc code=start
class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        diff = [0] * n
        diff[0] = nums[0]
        for i in range(1, n):
            diff[i] = nums[i] - nums[i - 1]
        print diff
# @lc code=end
[1,3,6]
6
