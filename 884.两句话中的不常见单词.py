#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start
from typing import Counter, List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        arr1, arr2 = s1.split(' '), s2.split(' ')
        cnt1, cnt2 = Counter(arr1), Counter(arr2)
        set1, set2 = set(arr1), set(arr2)
        ans = []
        for word in set1:
            if word not in set2 and cnt1[word] == 1:
                ans.append(word)
        for word in set2:
            if word not in set1 and cnt2[word] == 1:
                ans.append(word)
        return ans


# @lc code=end

s1 = "this apple is sweet"
s2 = "this apple is sour"
s1 = "apple apple"
s2 = "banana"
s1 = "s z z z s"
s2 = "s z ejt"
s = Solution()
print(s.uncommonFromSentences(s1, s2))