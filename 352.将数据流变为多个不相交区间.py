#
# @lc app=leetcode.cn id=352 lang=python3
#
# [352] 将数据流变为多个不相交区间
#

# @lc code=start
# 并查集
from sortedcontainers import SortedSet
class SummaryRanges:

    def __init__(self):
        self.find = [i for i in range(10002)]
        self.nums = SortedSet()


    def addNum(self, val: int) -> None:
        self.nums.add(val)
        self.find[val] = self.find[val + 1]
        

    def getIntervals(self) -> List[List[int]]:
        ans = []
        for num in self.nums:
            if ans and num <= ans[-1][1]: continue
            ans.append([num, self.f(num) - 1])
        return ans


    def f(self, x):
        if x == self.find[x]: return x
        self.find[x] = self.f(self.find[x])
        return self.find[x]



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
# @lc code=end

# 二分查找普通解法
class SummaryRanges:

    def __init__(self):
        self.range_list = []


    def addNum(self, val: int) -> None:
        N = len(self.range_list)
        if N == 0: self.range_list.append([val, val])
        # 二分查找
        l, r = 0, N - 1
        while l < r:
            mid = (l + r + 1) >> 1
            if self.range_list[mid][0] <= val: l = mid
            else: r = mid - 1
        
        cur = self.range_list[r]

        if cur[0] > val:
            if cur[0] + 1 == val: cur[0] = val
            else: self.range_list.insert(r, [val, val])
            return
        
        if cur[0] <= val <= cur[1]:
            return
        elif r == N - 1:
            if cur[1] + 1 == val: cur[1] = val
            else: self.range_list.append([val, val])
        else:
            nxt = self.range_list[r + 1]
            if cur[1] + 1 == val and val == nxt[0] - 1:
                cur[1] = nxt[1]
                self.range_list.pop(r + 1)
            elif cur[1] + 1 == val:
                cur[1] = val
            elif nxt[0] - 1 == val:
                nxt[0] = val
            else:
                self.range_list.insert(r + 1, [val, val])

    def getIntervals(self) -> List[List[int]]:
        N = len(self.range_list)
        ans = []
        for i in range(N): ans.append(self.range_list[i])
        return ans