#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#

# @lc code=start
from typing import List


class SegmentTree:
    def __init__(self, arr: List):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0 for _ in range(self.n << 2)]
        self.lazy = [0 for _ in range(self.n << 2)]
        self._build(0, self.n - 1, 0)

    def _ls(self, node: int) -> int:
        return (node << 1) + 1

    def _rs(self, node: int) -> int:
        return (node << 1) + 2

    def _push_up(self, node: int):
        self.tree[node] = self.tree[self._ls(node)] + self.tree[self._rs(node)]

    def _push_down(self, node: int, l: int, r: int):
        if self.lazy[node]:
            mid = (l + r) >> 1
            self.lazy[self._ls(node)] += self.lazy[node]
            self.lazy[self._rs(node)] += self.lazy[node]
            self.tree[self._ls(node)] += self.lazy[node] * (mid - l + 1)
            self.tree[self._rs(node)] += self.lazy[node] * (r - mid)
            self.lazy[node] = 0

    def _build(self, l: int, r: int, node: int):
        if l == r:
            self.tree[node] = self.arr[l]
            return

        mid = (l + r) >> 1
        self._build(l, mid, self._ls(node))
        self._build(mid + 1, r, self._rs(node))
        self._push_up(node)

    def _update(self, L: int, R: int, l: int, r: int, val: int, node: int):
        if L <= l and r <= R:
            self.tree[node] += val * (r - l + 1)
            self.lazy[node] += val
            return

        self._push_down(node, l, r)
        mid = (l + r) >> 1
        if L <= mid:
            self._update(L, R, l, mid, val, self._ls(node))
        if mid < R:
            self._update(L, R, mid + 1, r, val, self._rs(node))
        self._push_up(node)

    def _query(self, L: int, R: int, l: int, r: int, node: int) -> int:
        if L > r or R < l:
            return 0
        elif L <= l and r <= R:
            return self.tree[node]

        self._push_down(node, l, r)
        mid = (l + r) >> 1
        return self._query(L, R, l, mid, self._ls(node)) + self._query(L, R, mid + 1, r, self._rs(node))

    def update(self, L: int, R: int, val: int):
        self._update(L, R, 0, self.n - 1, val, 0)

    def query(self, L: int, R: int) -> int:
        return self._query(L, R, 0, self.n - 1, 0)



class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        _sum = 0
        pre_sums = [0]
        for num in nums:
            _sum += num
            pre_sums.append(_sum)
        all_nums = set()
        for x in pre_sums:
            all_nums.add(x)
            all_nums.add(x - lower)
            all_nums.add(x - upper)

        n = len(all_nums)
        mp = {num: i + 1 for num, i in zip(sorted(list(all_nums)), range(n))}

        ans = 0
        segt = SegmentTree([0 for _ in range(len(all_nums) + 1)])
        for x in pre_sums:
            left, right = mp[x - upper], mp[x - lower]
            ans += segt.query(left, right)
            segt.update(mp[x], mp[x], 1)
            
        return ans
        


# @lc code=end

