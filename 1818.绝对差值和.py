#
# @lc app=leetcode.cn id=1818 lang=python
#
# [1818] 绝对差值和
#

# @lc code=start
class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        nums = sorted(nums1)
        MOD = 10**9 + 7
        sums, maxn = 0, 0
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            sums = (sums + diff) % MOD
            # 二分查找已排序nums1中nums距离nums2[i]最近的点
            j = self.binarySearch(nums, nums2[i])
            if j < n:
                maxn = max(maxn, diff - (nums[j] - nums2[i]))
            if j > 0:
                maxn = max(maxn, diff - (nums2[i] - nums[j - 1]))
        
        return (sums - maxn + MOD) % MOD
    
    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1
        if nums[right] < target:
            return right + 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
# @lc code=end

