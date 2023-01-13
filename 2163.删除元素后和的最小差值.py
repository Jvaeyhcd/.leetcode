#
# @lc app=leetcode.cn id=2163 lang=python3
#
# [2163] 删除元素后和的最小差值
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 3
        min_pq = nums[m - n:]
        heapq.heapify(min_pq)
        # 最大后缀和
        suf_max = [0 for _ in range(m - n + 1)]
        suf_max[-1] = s = sum(min_pq)
        for i in range(m - n - 1, n - 1, -1):
            s += nums[i] - heapq.heappushpop(min_pq, nums[i])
            suf_max[i] = s
        
        max_pq = [-v for v in nums[:n]]
        heapq.heapify(max_pq)
        # 最小前缀和
        pre_min = -sum(max_pq)
        ans = pre_min - suf_max[n]
        for i in range(n, m - n):
            pre_min += nums[i] + heapq.heappushpop(max_pq, -nums[i])
            ans = min(ans, pre_min - suf_max[i + 1])
        return ans
# @lc code=end

S = Solution()
nums = [16,46,43,41,42,14,36,49,50,28,38,25,17,5,18,11,14,21,23,39,23]
ans = S.minimumDifference(nums)
print(ans)