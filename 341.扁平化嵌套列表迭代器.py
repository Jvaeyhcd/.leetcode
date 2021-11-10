#
# @lc app=leetcode.cn id=341 lang=python
#
# [341] 扁平化嵌套列表迭代器
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        n = len(nestedList)
        for i in range(n - 1, -1, -1):
            self.stack.append(nestedList[i])
        

    def next(self):
        """
        :rtype: int
        """
        cur = self.stack.pop(-1)
        return cur.getInteger()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            self.stack.pop()
            nestedList = cur.getList()
            for i in range(len(nestedList) - 1, -1, -1):
                self.stack.append(nestedList[i])
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

