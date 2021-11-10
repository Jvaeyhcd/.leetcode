#
# @lc app=leetcode.cn id=477 lang=python
#
# [477] 汉明距离总和
#

# @lc code=start
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = (10 ** 9).bit_length()
        # 记录1的个数
        arr = [0 for _ in range(l)]
        for num in nums:
            i = 0
            while num:
                arr[i] += num & 1
                i += 1
                num >>= 1
        
        ans = 0
        for a in arr:
            ans += (n - a) * a
        
        return ans
# @lc code=end

