#
# @lc app=leetcode.cn id=1787 lang=python
#
# [1787] 使所有区间的异或结果为零
#

# @lc code=start
class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MAXX = 1024

        n = len(nums)
        f = [float('inf')] * MAXX
        # 边界条件
        f[0] = 0

        for i in range(k):
            counter = Counter()
            size = 0
            for j in range(i, n, k):
                counter[nums[j]] += 1
                size += 1
            
            g = [min(f)] * MAXX
            for mask in range(MAXX):
                for x, count in counter.items():
                    g[mask] = min(g[mask], f[mask ^ x] - count)
            
            f = [val + size for val in g]
        
        return f[0]
# @lc code=end

