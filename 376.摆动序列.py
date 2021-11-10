#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
# 动态规划+空间优化
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        up = 1
        down = 1

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                down = max(down, up + 1)
            elif nums[i] > nums[i - 1]:
                up = max(up, down + 1)
        return max(up, down)
                

# @lc code=end

# 动态规划
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        # up[i]表示nums[0:i]中最后两个数字递增的最长摆动序列的长度
        # down[i]表示nums[0:i]中最后两个数字递减的最长摆动序列的长
        up = [0] * n
        down = [0] * n
        up[0] = 1
        down[0] = 1

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = max(down[i - 1], up[i - 1] + 1)
            elif nums[i] > nums[i - 1]:
                down[i] = down[i - 1]
                up[i] = max(up[i - 1], down[i - 1] + 1)
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        return max(up[n - 1], down[n - 1])