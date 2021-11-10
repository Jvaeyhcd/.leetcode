#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 迭代
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        n = len(postorder)
        root = TreeNode(postorder[-1])
        stack = [root]
        index = n - 1
        # 反序开始遍历
        for i in range(n - 2, -1, -1):
            val = postorder[i]
            node = stack[-1]
            # 指针index指向中序遍历的值与栈顶元素不同，将当前节点作为栈顶节点的右儿子
            if node.val != inorder[index]:
                node.right = TreeNode(val)
                stack.append(node.right)
            else:
                # 指针index指向中序遍历的值与栈顶元素相同，不断弹出栈顶节点并向左移动index指针
                while stack and stack[-1].val == inorder[index]:
                    node = stack.pop()
                    index -= 1
                # 将当前值作为最后一个弹出栈的节点的左儿子
                node.left = TreeNode(val)
                stack.append(node.left)
        return root

# @lc code=end

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 后序遍历的最后一个节点是根节点
        def build(poststart: int, postend: int, instart: int, inend: int) -> TreeNode:
            if instart > inend or poststart > postend: return None
            root = TreeNode(postorder[postend])
            # 找到中序遍历节点的位置，前半部分是左子树，后半部分是右子树
            for i in range(instart, inend + 1):
                if inorder[i] == postorder[postend]:
                    # 左子树节点个数
                    leftsize = i - instart
                    root.left = build(poststart, poststart + leftsize - 1, instart, i - 1)
                    root.right = build(poststart + leftsize, postend - 1, i + 1, inend)
            return root
        
        return build(0, len(postorder) - 1, 0, len(inorder) - 1)

# 递归（优化）
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        index = {value: index for index, value in enumerate(inorder)}
        # 后序遍历的最后一个节点是根节点
        def build(poststart: int, postend: int, instart: int, inend: int) -> TreeNode:
            if instart > inend or poststart > postend: return None
            root = TreeNode(postorder[postend])
            i = index[postorder[postend]]
            # 左子树节点个数
            leftsize = i - instart
            root.left = build(poststart, poststart + leftsize - 1, instart, i - 1)
            root.right = build(poststart + leftsize, postend - 1, i + 1, inend)
                    
            return root
        
        return build(0, len(postorder) - 1, 0, len(inorder) - 1)