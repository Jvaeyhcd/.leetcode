#
# @lc app=leetcode.cn id=456 lang=python
#
# [456] 132模式
#

# @lc code=start
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        left_min = [float('inf') for _ in range(N)]
        for i in range(1, N):
            left_min[i] = min(left_min[i - 1], nums[i - 1])
        
        stack = []
        for j in range(N - 1, -1, -1):
            numk = float('-inf')
            while stack and stack[-1] < nums[j]:
                numk = stack.pop()
            
            if left_min[j] < numk:
                return True
            
            stack.append(nums[j])
        
        return False
# @lc code=end

