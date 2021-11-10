#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        l = 0
        cur = head
        list_arr = []
        while cur:
            l += 1
            list_arr.append(cur)
            cur = cur.next
        ans = []

        len_arr = []
        if l % k == 0:
            len_arr = [l for _ in range(l // k + 1)]
        else:
            max_len, min_len = l // k + 1, l // k
            for i in range(k):
                total = 0
                ll = max_len if (l - total) > min_len * (k - i) else min_len
                len_arr.append(ll)
                total += ll
        print(len_arr)
        return ans
# @lc code=end

