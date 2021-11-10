#
# @lc app=leetcode.cn id=523 lang=python
#
# [523] 连续的子数组和
#

# @lc code=start
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False
        pre_map = collections.defaultdict(int)
        pre_map[0] = -1

        remainder = 0
        for i in range(n):
            remainder = (remainder + nums[i]) % k
            if remainder in pre_map:
                prev_index = pre_map[remainder]
                if i - prev_index > 1:
                    return True
            else:
                pre_map[remainder] = i
        return False
# @lc code=end

