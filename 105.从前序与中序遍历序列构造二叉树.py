#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        # 根节点一定是先序遍历的第一个节点
        root = TreeNode(preorder[0])
        # 栈初始存放根节点
        stack = [root]
        # 指向中序遍历第一个节点的指针
        index = 0
        for i in range(1, n):
            val = preorder[i]
            # 栈顶元素
            node = stack[-1]
            # 当前栈顶节点值与中序遍历的节点不同，我们将当前节点作为栈顶节点的左儿子
            if node.val != inorder[index]:
                node.left = TreeNode(val)
                stack.append(node.left)
            # 如果指针index指向中序遍历的节点恰好是栈顶节点
            else:
                # 不断弹出栈顶节点并向右移动index指针
                while stack and stack[-1].val == inorder[index]:
                    node = stack.pop()
                    index += 1
                # 当前值为最后一个弹出节点的右子树
                node.right = TreeNode(val)
                stack.append(node.right)
        return root

# @lc code=end

# 递归（Hash优化）
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 存储中序遍历节点的位置信息
        index = {value: index for index, value in enumerate(inorder)}
        def build(prestart: int, preend: int, instart: int, inend: int) -> TreeNode:
            if prestart > preend or instart > inend: return None
            # 先序遍历的第一个点是根节点
            node = TreeNode(preorder[prestart])
            # 找到中序遍历中节点的位置，找到该位置后，位置前后分别是左右两个节点
            # 这里使用hash表存储节点的位置信息可以快速找到节点
            i = index[preorder[prestart]]
            # 左边子树节点的个数
            leftsize = i - instart
            node.left = build(prestart + 1, prestart + leftsize, instart, i - 1)
            node.right = build(prestart + leftsize + 1, preend, i + 1, inend)
            return node
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

# 递归（朴素）
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def build(prestart: int, preend: int, instart: int, inend: int) -> TreeNode:
            if prestart > preend or instart > inend: return None
            # 先序遍历的第一个点是根节点
            node = TreeNode(preorder[prestart])
            # 找到中序遍历中节点的位置，找到该位置后，位置前后分别是左右两个节点
            for i in range(instart, inend + 1):
                if preorder[prestart] == inorder[i]:
                    # 左边子树节点的个数
                    leftsize = i - instart
                    node.left = build(prestart + 1, prestart + leftsize, instart, i - 1)
                    node.right = build(prestart + leftsize + 1, preend, i + 1, inend)
            return node
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop: TreeNode):
            if inorder and inorder[0] != stop:
                root = TreeNode(preorder.pop(0))
                root.left = build(root.val)
                inorder.pop(0)
                root.right = build(stop)
                return root
        
        return build(None)

