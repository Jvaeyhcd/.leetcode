#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur, pre = None, head
        i = 0

        arr = []
        while i < k and pre:
            tmp = pre.next
            pre.next = cur
            cur, pre = pre, tmp
            i += 1
            if i == k:
                i = 0
                arr.append(cur)
                cur = None
        
        if cur: 
            pre = cur
            cur = None
            while pre:
                tmp = pre.next
                pre.next = cur
                cur, pre = pre, tmp
            arr.append(cur)
        dummy = ListNode()
        cur = dummy
        for node in arr:
            cur.next = node
            while cur.next:
                cur = cur.next
        
        return dummy.next

# @lc code=end

