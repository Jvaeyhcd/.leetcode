#
# @lc app=leetcode.cn id=497 lang=python3
#
# [497] 非重叠矩形中的随机点
#

# @lc code=start
from random import randrange
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects


    def pick(self) -> List[int]:
        ans = [self.rects[0][0], self.rects[0][1]]
        cnt = 0
        for a, b, x, y in self.rects:
            w, h = (x - a + 1), (y - b + 1)
            cnt += w * h
            if 0 <= randrange(cnt) < w * h:
                r = randrange(w * h)
                ans = [r % w + a, r // w + b]
        return ans



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# @lc code=end

