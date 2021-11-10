#
# @lc app=leetcode.cn id=449 lang=python3
#
# [449] 序列化和反序列化二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return 'X'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def buildTree(arr: list) -> TreeNode:
            val = arr.pop(0)
            if val == 'X': return None
            root = TreeNode(int(val))
            root.left = buildTree(arr)
            root.right = buildTree(arr)
            return root
        return buildTree(data.split(','))


        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

