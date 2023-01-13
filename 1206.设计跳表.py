#
# @lc app=leetcode.cn id=1206 lang=python3
#
# [1206] 设计跳表
#

# @lc code=start
import random

class Node:
    def __init__(self, val, level) -> None:
        self.data = val
        self.deeps = [None for _ in range(level)]


class Skiplist:

    def __init__(self):
        self.max_level = 16
        self.p = 0.5
        self.level = 1
        self.head = Node(None, self.max_level)


    def random_level(self):
        level = 1
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level


    def search(self, target: int) -> bool:
        cur = self.head
        for i in range(self.level - 1, -1, -1):
            while cur.deeps[i] and cur.deeps[i].data < target:
                cur = cur.deeps[i]
        
        if cur.deeps[0] and cur.deeps[0].data == target:
            return True
        return False


    def add(self, num: int) -> None:
        level = self.random_level()
        if self.level < level:
            self.level = level
        
        new_node = Node(num, level)
        cache = [None for _ in range(level)]
        cur = self.head

        for i in range(level - 1, -1, -1):
            while cur.deeps[i] and cur.deeps[i].data < num:
                cur = cur.deeps[i]
            cache[i] = cur

        for i in range(level):
            new_node.deeps[i] = cache[i].deeps[i]
            cache[i].deeps[i] = new_node


    def erase(self, num: int) -> bool:
        cache = [None for _ in range(self.level)]
        cur = self.head

        for i in range(self.level - 1, -1, -1):
            while cur.deeps[i] and cur.deeps[i].data < num:
                cur = cur.deeps[i]
            cache[i] = cur

        if cur.deeps[0] and cur.deeps[0].data == num:
            for i in range(self.level):
                if cache[i].deeps[i] and cache[i].deeps[i].data == num:
                    cache[i].deeps[i] = cache[i].deeps[i].deeps[i]
            return True
        return False



# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end

