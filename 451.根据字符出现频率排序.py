#
# @lc app=leetcode.cn id=451 lang=python
#
# [451] 根据字符出现频率排序
#

# @lc code=start
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        map = collections.defaultdict(int)
        max_count = 0
        for c in s:
            map[c] += 1
            max_count = max(max_count, map[c])
        
        bucket = collections.defaultdict(list)
        for k in map.keys():
            v = map[k]
            bucket[v].append(k)
        
        ans = ''
        for i in range(max_count, 0, -1):
            if bucket[i]:
                for c in bucket[i]:
                    ans += (c * i)
        
        return ans

            
# @lc code=end

