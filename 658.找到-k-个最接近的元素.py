#
# @lc app=leetcode.cn id=658 lang=python
#
# [658] 找到 K 个最接近的元素
#

# @lc code=start
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(arr)
        pos = self.findClosestIndex(arr, x)

        # 二分查找得到的点不一定是距离x最近的点，所以取其左右距离x更近的点
        if pos > 0 and abs(arr[pos - 1] - x) <= abs(arr[pos] - x):
            pos -= 1
        elif pos < n - 1 and abs(arr[pos] - x) > abs(arr[pos + 1] - x):
            pos += 1

        ans = []
        l, r = pos, pos
        i = 0
        while i < k and not (l < 0 and r >= n):
            if r < n and (abs(arr[r] - x) < abs(arr[l] - x) or l < 0):
                ans.append(arr[r])
                r += 1
            else:
                if l == r:
                    r += 1
                ans.insert(0, arr[l])
                l -= 1
            i += 1
        return ans
    
    # 找打距离x最近的点
    def findClosestIndex(self, arr, x):
        n = len(arr)
        l, r = 0, n - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if arr[mid] > x:
                r = mid - 1
            elif arr[mid] < x:
                l = mid + 1
            else:
                return mid
        
        return l
# @lc code=end
[1,2,3,4,5]
4
3
[1,2,3,4,5]
4
-1
[0,1,1,1,2,3,6,7,8,9]
9
4
[1,1,1,10,10,10]
1
9
[0,0,1,2,3,3,4,7,7,8]
3
5
[1,3]
1
2
[1,5,10]
1
4