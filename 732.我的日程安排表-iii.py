#
# @lc app=leetcode.cn id=732 lang=python3
#
# [732] 我的日程安排表 III
#

# @lc code=start
import collections


class MyCalendarThree:

    def __init__(self):
        self.mp = collections.defaultdict(lambda:0)


    def book(self, start: int, end: int) -> int:
        self.mp[start] += 1
        self.mp[end] -= 1

        ans, active = 0, 0
        for k in sorted(self.mp):
            active += self.mp[k]
            ans = max(ans, active)
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
# @lc code=end

