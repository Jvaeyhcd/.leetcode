#
# @lc app=leetcode.cn id=138 lang=python
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):

    def __init__(self):
        self.node_map = collections.defaultdict(Node)
        
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        if head not in self.node_map:
            new_head = Node(head.val)
            self.node_map[head] = new_head
            new_head.next = self.copyRandomList(head.next)
            new_head.random = self.copyRandomList(head.random)
        
        return self.node_map[head]

        
# @lc code=end

