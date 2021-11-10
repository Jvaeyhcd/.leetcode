#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        FLAG_LEFT = 0
        FLAG_RIGHT = 1

        def dfs(root: TreeNode, prev: TreeNode, flag: int):
            if not root: return
            if root.val == key:
                # 找到了结果
                left, right, node = root.left, root.right, None

                if left and right:
                    # 删除节点同时存在左右两个子树
                    # 将右子树作为根节点，并将左子树放在右子树的左叶子节点上
                    tmp = right
                    c, p = tmp.left, None
                    while c:
                        p = c
                        c = c.left
                    if p:
                        p.left = left
                    else:
                        tmp.left = left
                    node = tmp
                elif left:
                    node = left
                elif right:
                    node = right

                if flag == FLAG_RIGHT: prev.right = node
                elif flag == FLAG_LEFT: prev.left = node
                return
                
            elif root.val < key:
                # 去右子树中找
                dfs(root.right, root, FLAG_RIGHT)
            else:
                # 去左子树中找
                dfs(root.left, root, FLAG_LEFT)
        dummy = TreeNode(0)
        dummy.left = root

        dfs(dummy.left, dummy, FLAG_LEFT)
        
        return dummy.left
# @lc code=end

