#
# @lc app=leetcode.cn id=519 lang=python3
#
# [519] 随机翻转矩阵
#

# @lc code=start
from typing import List
import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        # 题目数据量大所以不能用数组，换成字典
        self.map = {}

    def flip(self) -> List[int]:
        x = random.randint(0, self.total - 1)
        self.total -= 1
        # 查找位置 x 对应的映射
        idx = self.map.get(x, x)
        # 将位置 x 对应的映射设置为位置 total 对应的映射
        self.map[x] = self.map.get(self.total, self.total)
        return [idx // self.n, idx % self.n]
        
    def reset(self) -> None:
        self.total = self.m * self.n
        self.map.clear()



# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
# @lc code=end

