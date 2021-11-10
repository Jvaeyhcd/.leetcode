#
# @lc app=leetcode.cn id=1239 lang=python
#
# [1239] 串联字符串的最大长度
#

# @lc code=start
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        ans = 0
        masks = [0]
        for s in arr:
            mask = 0
            for c in s:
                idx = ord(c) - ord('a')
                if (mask >> idx) & 1:
                    mask = 0
                    break
                mask |= 1 << idx

            if mask == 0:
                continue

            n = len(masks)
            for i in range(n):
                m = masks[i]
                if m & mask == 0:
                    masks.append(m | mask)
                    ans = max(ans, bin(m | mask).count('1'))
        
        return ans
# @lc code=end

