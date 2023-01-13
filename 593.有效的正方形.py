#
# @lc app=leetcode.cn id=593 lang=python3
#
# [593] 有效的正方形
#

# @lc code=start
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        def check_length(v1: List[int], v2: List[int]) -> bool:
            return v1[0] * v1[0] + v1[1] * v1[1] == v2[0] * v2[0] + v2[1] * v2[1]

        def check_mid_point(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
            return p1[0] + p2[0] == p3[0] + p4[0] and p1[1] + p2[1] == p3[1] + p4[1]

        def check_cos(v1: List[int], v2: List[int]) -> bool:
            return v1[0] * v2[0] + v1[1] * v2[1] == 0

        def check(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
            v1 = [p1[0] - p2[0], p1[1] - p2[1]]
            v2 = [p3[0] - p4[0], p3[1] - p4[1]]
            return check_length(v1, v2) and check_mid_point(p1, p2, p3, p4) and check_cos(v1, v2)

        if p1 == p2:
            return False
        if check(p1, p2, p3, p4):
            return True
        if p1 == p3:
            return False
        if check(p1, p3, p2, p4):
            return True
        if p1 == p4:
            return False
        if check(p1, p4, p2, p3):
            return True
        return False
# @lc code=end

