#
# @lc app=leetcode.cn id=421 lang=python
#
# [421] 数组中两个数的最大异或值
#

# @lc code=start
class Trie(object):
    def __init__(self):
        # 左子树指向表示 0 的节点
        self.left = None
        # 右子树指向表示 1 的节点
        self.right = None
        
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 字典树的根节点
        root = Trie()
        # 最高位的二进制编号为30
        HIGH_BIG = 30

        def add(num):
            cur = root
            for k in range(HIGH_BIG, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    if not cur.left:
                        cur.left = Trie()
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Trie()
                    cur = cur.right
        
        def check(num):
            cur = root
            x = 0
            for k in range(HIGH_BIG, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    # a_i 的第 k 个二进制位为 0，应当往表示 1 的子节点 right 走
                    if cur.right:
                        cur = cur.right
                        x = (x << 1) + 1
                    else:
                        cur = cur.left
                        x <<= 1
                else:
                    # a_i 的第 k 个二进制位为 1，应当往表示 0 的子节点 left 走
                    if cur.left:
                        cur = cur.left
                        x = (x << 1) + 1
                    else:
                        cur = cur.right
                        x <<= 1
            
            return x
        
        n = len(nums)
        x = 0
        for i in range(1, n):
            # 将 nums[i-1] 放入字典树，此时 nums[0 .. i-1] 都在字典树中
            add(nums[i - 1])
            # 将 nums[i] 看作 ai，找出最大的 x 更新答案
            x = max(x, check(nums[i]))
        
        return x


# @lc code=end

