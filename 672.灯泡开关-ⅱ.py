#
# @lc app=leetcode.cn id=672 lang=python3
#
# [672] 灯泡开关 Ⅱ
#

# @lc code=start
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n == 1:
            return 2
        elif n == 2:
            return 3 if presses == 1 else 4
        else:
            return 4 if presses == 1 else (7 if presses == 2 else 8)
# @lc code=end

