#
# @lc app=leetcode.cn id=731 lang=python3
#
# [731] 我的日程安排表 II
#

# @lc code=start
import collections


class MyCalendarTwo:

    def __init__(self):
        self.mp = collections.defaultdict(lambda:0)


    def book(self, start: int, end: int) -> bool:
        self.mp[start] += 1
        self.mp[end] -= 1

        active = 0
        for k in sorted(self.mp):
            active += self.mp[k]
            if active > 2:
                self.mp[start] -= 1
                self.mp[end] += 1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end

