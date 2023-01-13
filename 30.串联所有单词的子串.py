#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
from typing import List
import random
import collections


# Rabin-Karp字符串匹配算法
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        L = len(words[0])
        if len(s) < L:
            return []

        BASE_1 = random.randint(26, 100)
        BASE_2 = random.randint(26, 100)
        MOD_1 = random.randint(10**9+7, 2**31-1)
        MOD_2 = random.randint(10**9+7, 2**31-1)

        table = {chr(ord('a') + i): i for i in range(26)}
        cnts = collections.defaultdict(lambda:0)
        
        for i in range(n):
            mask_1, mask_2 = 0, 0
            for c in words[i]:
                mask_1 = (mask_1 * BASE_1 + table[c]) % MOD_1
                mask_2 = (mask_2 * BASE_2 + table[c]) % MOD_2
            cnts[(mask_1, mask_2)] += 1
        
        word_set = set(cnts.keys())

        mask_1, mask_2 = 0, 0
        power_1, power_2 = pow(BASE_1, L, MOD_1), pow(BASE_2, L, MOD_2)
        arr = list(s)
        for i in range(L):
            mask_1 = (mask_1 * BASE_1 + table[arr[i]]) % MOD_1
            mask_2 = (mask_2 * BASE_2 + table[arr[i]]) % MOD_2
        
        prefix = [(mask_1, mask_2)]
        for i in range(1, len(s) - L + 1):
            mask_1 = (mask_1 * BASE_1 - table[arr[i - 1]] * power_1 + table[arr[i + L - 1]]) % MOD_1
            mask_2 = (mask_2 * BASE_2 - table[arr[i - 1]] * power_2 + table[arr[i + L - 1]]) % MOD_2
            prefix.append((mask_1, mask_2))
            
        # print(len(s), len(prefix), n, L)
        ans = []
        for i in range(len(s) - n * L + 1):
            tmp = {k: v for k, v in cnts.items()}
            j = i
            found = True
            while j < i + n * L:
                if prefix[j] not in word_set or tmp[prefix[j]] == 0:
                    found = False
                    break
                tmp[prefix[j]] -= 1
                j += L
            # print(tmp)
            if found and all(v == 0 for _, v in tmp.items()):
                ans.append(i)
        
        return ans
        
# @lc code=end

