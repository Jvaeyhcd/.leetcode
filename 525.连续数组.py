#
# @lc app=leetcode.cn id=525 lang=python
#
# [525] 连续数组
#

# @lc code=start
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        counter_map = collections.defaultdict(int)
        counter = 0
        counter_map[0] = -1
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num == 1:
                counter += 1
            else:
                counter -= 1
            
            if counter_map.has_key(counter):
                prev_index = counter_map[counter]
                res = max(res, i - prev_index)
            else:
                counter_map[counter] = i
        
        return res
# @lc code=end

