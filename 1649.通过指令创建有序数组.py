#
# @lc app=leetcode.cn id=1649 lang=python3
#
# [1649] 通过指令创建有序数组
#

# @lc code=start
import collections
from typing import List


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        arr = [k for k, _ in collections.Counter(instructions).items()]
        n = len(arr)
        BIT = FenwickTree(n)
        h = [i for i in range(n)]
        h.sort(key=lambda x:arr[x])
        mp = collections.defaultdict(int)
        for i in range(n):
            mp[arr[h[i]]] = i + 1

        ans = 0
        cnt = collections.defaultdict(lambda:0)
        for i, num in enumerate(instructions):
            index = mp[num]
            BIT.update(index, 1)
            # 当前num出现的次数
            cnt[num] += 1
            # 当前小于等于num的个数
            a = BIT.query(index)
            # 当前大于num的个数
            b = BIT.query(n) - a
            # print(index, num, a, b, cnt[num])
            ans += min(a - cnt[num], b)
            ans %= 1000000007
            
        return ans


class FenwickTree:
    def __init__(self, n: int):
        self.bit_arr = [0] * (n + 1)


    def lowbit(self, x: int) -> int:
        return x & (-x)
    
    
    def update(self, idx: int, delta: int):
        n = len(self.bit_arr)
        while idx < n:
            self.bit_arr[idx] += delta
            idx += self.lowbit(idx)
    

    def query(self, idx: int) -> int:
        ans = 0
        while idx:
            ans += self.bit_arr[idx]
            idx -= self.lowbit(idx)
        return ans
# @lc code=end

