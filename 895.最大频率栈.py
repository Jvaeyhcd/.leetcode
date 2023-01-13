#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#

# @lc code=start
import collections


class FreqStack:

    def __init__(self):
        self.cnts = collections.defaultdict(int)
        self.group = collections.defaultdict(list)
        self.maxcnt = 0

    def push(self, val: int) -> None:
        cnt = self.cnts[val] + 1
        self.cnts[val] = cnt
        if cnt > self.maxcnt:
            self.maxcnt = cnt
        self.group[cnt].append(val)


    def pop(self) -> int:
        x = self.group[self.maxcnt].pop()
        self.cnts[x] -= 1
        if not self.group[self.maxcnt]:
            self.maxcnt -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

