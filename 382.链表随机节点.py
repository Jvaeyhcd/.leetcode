#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
from random import randrange


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head


    def getRandom(self) -> int:
        ans = 0
        cnt = 0
        cur = self.head
        while cur:
            cnt += 1
            if randrange(0, cnt) == 0:
                ans = cur
            cur = cur.next
        return ans.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

