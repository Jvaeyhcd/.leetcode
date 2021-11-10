#
# @lc app=leetcode.cn id=1723 lang=python
#
# [1723] 完成所有工作的最短时间
#

# @lc code=start
class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        jobs.sort()
        low, high = 0, len(jobs) - 1
        while low < high:
            tmp = jobs[low]
            jobs[low] = jobs[high]
            jobs[high] = tmp
            low += 1
            high -= 1
        
        print jobs
        l, r = max(jobs), sum(jobs)
        while l < r:
            mid = (l + r) >> 1
            if self.check(jobs, k, mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        
    def check(self, jobs, k, limit):
        workloads = [0] * k
        return self.backtrack(jobs, workloads, 0, limit)
    

    def backtrack(self, jobs, workloads, i, limit):
        if i >= len(jobs):
            return True
        
        cur = jobs[i]
        for j in range(len(workloads)):
            if workloads[j] + cur <= limit:
                workloads[j] += cur
                if self.backtrack(jobs, workloads, i + 1, limit):
                    return True
                workloads[j] -= cur
            
            if workloads[j] == 0 or workloads[j] + cur == limit:
                break
        
        return False
# @lc code=end

