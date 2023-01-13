#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
from random import choice


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.indexs = {}


    def insert(self, val: int) -> bool:
        if val in self.indexs:
            return False
        self.indexs[val] = len(self.nums)
        self.nums.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.indexs:
            return False
        idx = self.indexs[val]
        self.nums[idx] = self.nums[-1]
        self.indexs[self.nums[idx]] = idx
        self.nums.pop()
        del self.indexs[val]
        return True


    def getRandom(self) -> int:
        return choice(self.nums)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

