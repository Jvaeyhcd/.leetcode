#
# @lc app=leetcode.cn id=1780 lang=python3
#
# [1780] 判断一个数字是否可以表示成三的幂的和
#

# @lc code=start
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 2: return False
            n //= 3
        return True
# @lc code=end

