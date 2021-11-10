#
# @lc app=leetcode.cn id=560 lang=python
#
# [560] 和为K的子数组
#

# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 前缀和出现的次数
        pre_map = collections.defaultdict(int)
        pre_map[0] = 1
        cur_sum = 0
        ans = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in pre_map:
                ans += pre_map[cur_sum - k]
            pre_map[cur_sum] += 1
        return ans
# @lc code=end

