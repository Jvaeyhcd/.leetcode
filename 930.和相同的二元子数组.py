#
# @lc app=leetcode.cn id=930 lang=python
#
# [930] 和相同的二元子数组
#

# @lc code=start
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        n = len(nums)
        left1, left2, right = 0, 0, 0
        sum1, sum2 = 0, 0
        ans = 0
        while right < n:
            sum1 += nums[right]
            while left1 <= right and sum1 > goal:
                sum1 -= nums[left1]
                left1 += 1
            
            sum2 += nums[right]
            while left2 <= right and sum2 >= goal:
                sum2 -= nums[left2]
                left2 += 1
            
            ans += (left2 - left1)
            right += 1
        
        return ans

# @lc code=end

