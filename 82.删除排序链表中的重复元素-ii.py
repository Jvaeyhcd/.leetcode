#
# @lc app=leetcode.cn id=82 lang=python
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
        else:
            nxt = head.next
            while nxt and head.val == nxt.val:
                nxt = nxt.next
            return self.deleteDuplicates(nxt)
        return head
# @lc code=end

