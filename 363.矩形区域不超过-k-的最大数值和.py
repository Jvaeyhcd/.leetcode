#
# @lc app=leetcode.cn id=363 lang=python
#
# [363] 矩形区域不超过 K 的最大数值和
#

# @lc code=start
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        from sortedcontainers import SortedList
        m, n = len(matrix), len(matrix[0])
        sums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sums[i][j] = sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1] + matrix[i - 1][j - 1]
        
        ans = float('-inf')

        # 上边界
        for t in range(1, m + 1):
            # 下边界
            for b in range(t, m + 1):
                sl = SortedList()
                sl.add(0)
                for r in range(1, n + 1):
                    right = sums[b][r] - sums[t - 1][r]
                    left = sl.bisect_left(right - k)
                    # print left
                    if left != len(sl):
                        ans = max(ans, right - sl[left])
                    sl.add(right)
        
        return ans



# @lc code=end

