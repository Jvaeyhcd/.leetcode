#
# @lc app=leetcode.cn id=1177 lang=python
#
# [1177] 构建回文串检测
#

# @lc code=start
class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # 位运算统计奇偶数，cnts中第i个数表示s中前i个字符中出现的字符的奇偶数，1表示出现奇次数，0表示出现偶次数
        cnts = [0]
        for i, c in enumerate(s):
            cnts.append(cnts[i] ^ (1 << ord(c) - ord('a')))
        
        ans = []
        for (l, r, k) in queries:
            # 前缀和思想计算下标l到下标r间字符出现的奇偶数
            temp = cnts[l] ^ cnts[r + 1]
            # 统计二进制中1出现的次数就是奇数的个数
            cnt = bin(temp).count('1')
            ans.append(False if cnt // 2 > k else True)
        return ans

    # def canMakePaliQueries(self, s, queries):
    #     """
    #     :type s: str
    #     :type queries: List[List[int]]
    #     :rtype: List[bool]
    #     """
    #     # 哈希表存储前i个子串中每个字符出现的次数
    #     cnts = collections.defaultdict(lambda: defaultdict(int))
    #     n = len(s)
    #     for i in range(n):
    #         if i > 0:
    #             cnts[i] = copy.deepcopy(cnts[i - 1])
    #         cnts[i][s[i]] += 1
        
    #     ans = []
    #     for l, r, k in queries:
    #         # 子串中每个字符出现的次数
    #         letter_cnts = collections.defaultdict(int)
    #         if l == 0:
    #             letter_cnts = cnts[r]
    #         else:
    #             for key in cnts[r].keys():
    #                 letter_cnts[key] = cnts[r][key] - cnts[l][key]
    #         # 奇数的个数
    #         odd = 0
    #         for c in letter_cnts.keys():
    #             if letter_cnts[c] % 2 == 1:
    #                 odd += 1
    #         span = r - l + 1
    #         if span % 2 == 0:
    #             ans.append(odd // 2 <= k)
    #         else:
    #             ans.append(odd // 2 <= k + 1)
        
    #     return ans
                
# @lc code=end

