#
# @lc app=leetcode.cn id=517 lang=python3
#
# [517] 超级洗衣机
#

# @lc code=start
# 贪心算法
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n != 0: return -1
        avg = total // n
        ans, s = 0, 0
        for num in machines:
            num -= avg
            s += num
            ans = max(ans, abs(s), num)
        return ans

# @lc code=end

