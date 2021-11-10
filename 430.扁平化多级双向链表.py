#
# @lc app=leetcode.cn id=430 lang=python3
#
# [430] 扁平化多级双向链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

# 先序遍历迭代
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        stack = [head]
        dummy = Node()
        dummy.next = head
        stack = [dummy.next]
        cur, prev = None, None
        while stack:
            node = stack.pop()
            if not node:
                node = stack.pop()
                cur = node
                if prev:
                    prev.next = cur
                    prev.child = None
                    cur.prev = prev
                prev = cur
            else:
                if node.next: stack.append(node.next)
                if node.child: stack.append(node.child)
                stack.append(node)
                stack.append(None)
        
        return dummy.next
        
# @lc code=end

# 先序遍历递归
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.arr = []
        def preorder(node: 'Node'):
            if not node: return
            self.arr.append(node)
            preorder(node.child)
            preorder(node.next)
        if not head: return head
        preorder(head)
        for i in range(len(self.arr)):
            # print(self.arr[i].val)
            if i < len(self.arr) - 1:
                self.arr[i].next = self.arr[i + 1]
                self.arr[i + 1].prev = self.arr[i]
                self.arr[i].child = None
        
        self.arr[-1].child = None
        
        return self.arr[0]

