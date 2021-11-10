#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnts = collections.defaultdict(lambda:0)
        for num in nums1:
            cnts[num] += 1
        
        ans = []
        for num in nums2:
            if cnts[num] > 0:
                cnts[num] -= 1
                ans.append(num)
        
        return ans

# @lc code=end

