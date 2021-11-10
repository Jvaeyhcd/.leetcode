#
# @lc app=leetcode.cn id=173 lang=python
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def inOrder(self, root, arr):
        if not root:
            return
        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.queue = []
        stack = [root]
        # 迭代中序遍历
        while stack:
            node = stack.pop()
            if node is None:
                node = stack.pop()
                self.queue.append(node.val)
            else:
                if node.right: stack.append(node.right)
                stack.append(node)
                stack.append(None)
                if node.left: stack.append(node.left)

    def next(self):
        """
        :rtype: int
        """
        return self.queue.pop(0)


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

