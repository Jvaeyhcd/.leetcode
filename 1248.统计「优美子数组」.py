#
# @lc app=leetcode.cn id=1248 lang=python
#
# [1248] 统计「优美子数组」
#

# @lc code=start
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        arr = [-1]
        for i, n in enumerate(nums):
            if n & 1:
                arr.append(i)
        arr.append(len(nums))
        if len(arr) < k + 2:
            return 0
        
        for i in range(1, len(arr) - k):
            res = res + (arr[i] - arr[i - 1]) * (arr[i + k] - arr[i + k - 1])
        return res

# @lc code=end

