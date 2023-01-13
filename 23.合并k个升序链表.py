#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = []
        heapq.heapify(q)
        for node in lists:
            cur = node
            while cur:
                heapq.heappush(q, cur.val)
                cur = cur.next
        
        dummy = ListNode()
        cur = dummy
        while q:
            val = heapq.heappop(q)
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
# @lc code=end

