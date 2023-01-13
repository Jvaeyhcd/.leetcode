#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None,"
        ans = str(root.val) + ","
        ans += self.serialize(root.left)
        ans += self.serialize(root.right)
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = []
        s = ""
        for ch in data:
            if ch == ",":
                arr.append(s)
                s = ""
            else:
                s += ch
        if s != "":
            arr.append(s)
        return self.rdeserialize(arr)

    def rdeserialize(self, arr):
        if arr[0] == "None":
            arr.pop(0)
            return None
        root = TreeNode(int(arr[0]))
        arr.pop(0)
        root.left = self.rdeserialize(arr)
        root.right = self.rdeserialize(arr)
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

