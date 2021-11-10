#
# @lc app=leetcode.cn id=220 lang=python
#
# [220] 存在重复元素 III
#

# @lc code=start
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        bucket = {}
        size = t + 1
        for i in range(len(nums)):
            x = nums[i]
            idx = self.getBucketId(x, size)

            if idx in bucket:
                return True
            
            # 前一个桶是否存在满足条件的元素
            if idx - 1 in bucket and abs(x - bucket[idx - 1]) <= t:
                return True

            # 后一个桶是否存在满足条件的元素
            if idx + 1 in bucket and abs(x - bucket[idx + 1]) <= t:
                return True
            
            # 建立目标桶
            bucket[idx] = x

            # 维护桶的个数
            if i >= k:
                bucket.pop(self.getBucketId(nums[i - k], size))
        
        return False

    # 得到当前元素所在的桶的ID
    def getBucketId(self, x, w):
        if x < 0:
            return (x + 1) // w - 1
        else:
            return x // w
# @lc code=end

