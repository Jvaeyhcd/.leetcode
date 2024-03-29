#
# @lc app=leetcode.cn id=1707 lang=python
#
# [1707] 与数组中元素的最大异或值
#

# @lc code=start
class Trie(object):
    L = 30

    def __init__(self):
        self.left = None
        self.right = None


    def insert(self, val):
        node = self
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1
            if bit == 0:
                if not node.left:
                    node.left = Trie()
                node = node.left
            else:
                if not node.right:
                    node.right = Trie()
                node = node.right
    
    def getMaxXor(self, val):
        ans, node = 0, self
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1
            check = False
            if bit == 0:
                if node.right:
                    node = node.right
                    check = True
                else:
                    node = node.left
            else:
                if node.left:
                    node = node.left
                    check = True
                else:
                    node = node.right
            
            if check:
                ans |= 1 << i
        
        return ans



class Solution(object):
    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n, q = len(nums), len(queries)
        nums.sort()
        queries = sorted([(x, m, i) for i, (x, m) in enumerate(queries)], key=lambda query: query[1])
        # print queries
        ans = [0] * q
        t = Trie()

        idx = 0
        for x, m, qid in queries:
            while idx < n and nums[idx] <= m:
                t.insert(nums[idx])
                idx += 1
            if idx == 0:
                ans[qid] = -1
            else:
                ans[qid] = t.getMaxXor(x)
        
        return ans
# @lc code=end

