#
# @lc app=leetcode.cn id=457 lang=python
#
# [457] 环形数组是否存在循环
#

# @lc code=start
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        def next_pos(index):
            return (index + nums[index] + n) % n

        for i in range(n):
            slow = i
            fast = next_pos(slow)
            while nums[fast] * nums[i] > 0 and nums[next_pos(fast)] * nums[i] > 0:
                if fast == slow:
                    if slow == next_pos(slow):
                        break
                    return True
                slow = next_pos(slow)
                fast = next_pos(next_pos(fast))
        
        return False
# @lc code=end

