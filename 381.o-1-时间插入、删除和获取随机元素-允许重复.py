#
# @lc app=leetcode.cn id=381 lang=python3
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#

# @lc code=start
import collections
from random import choice


class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.indexs = collections.defaultdict(lambda:set())


    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.indexs[val].add(len(self.nums) - 1)
        return len(self.indexs[val]) == 1


    def remove(self, val: int) -> bool:
        if val not in self.indexs:
            return False
        idx = list(self.indexs[val])[0]
        last = self.nums[-1]
        if idx == len(self.nums) - 1:
            self.indexs[val].remove(idx)
            if len(self.indexs[val]) == 0:
                del self.indexs[val]
            self.nums.pop()
            return True
        self.nums[idx] = last
        self.indexs[val].remove(idx)
        self.indexs[last].remove(len(self.nums) - 1)
        if idx < len(self.nums) - 1:
            self.indexs[last].add(idx)
        if len(self.indexs[val]) == 0:
            del self.indexs[val]
        self.nums.pop()
        return True


    def getRandom(self) -> int:
        return choice(self.nums)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

