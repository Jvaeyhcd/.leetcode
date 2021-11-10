#
# @lc app=leetcode.cn id=368 lang=python
#
# [368] 最大整除子集
#

# @lc code=start
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        dp = [1] * n

        max_size = 1
        max_val = dp[0]

        # 第一步，动态规划找出最大子集的个数、最大子集中的最大整数
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            
            if dp[i] > max_size:
                max_size = dp[i]
                max_val = nums[i]
        
        # 第二步，倒推获得最大子集
        res = []
        if max_size == 1:
            res.append(nums[0])
            return res
        
        i = n - 1
        while i >= 0 and max_size > 0:
            if dp[i] == max_size and max_val % nums[i] == 0:
                res.append(nums[i])
                max_val = nums[i]
                max_size -= 1
            
            i -= 1
        
        return res

# @lc code=end

