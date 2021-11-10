#
# @lc app=leetcode.cn id=1711 lang=python
#
# [1711] 大餐计数
#

# @lc code=start
class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        power_of_two = [2 ** i for i in range(22)]
        cnts = collections.Counter(deliciousness)
        ans = 0
        for num1 in cnts:
            for cur in power_of_two:
                num2 = cur - num1
                # 折半，只算num1小于num2的情况，因为当num2大于num1的时候计算就重复
                if num2 in cnts and num1 <= num2:
                    if num1 == num2:
                        ans += ((cnts[num1] * (cnts[num1] - 1)) // 2)
                    else:
                        ans += cnts[num1] * cnts[num2]
        
        return ans % MOD

    # # 加法叠加
    # def countPairs(self, deliciousness):
    #     """
    #     :type deliciousness: List[int]
    #     :rtype: int
    #     """
    #     MOD = 10 ** 9 + 7
    #     power_of_two = [2 ** i for i in range(22)]
    #     cnts = collections.Counter()
    #     ans = 0
    #     for num in deliciousness:
    #         for target in power_of_two:
    #             ans += cnts[target - num]
    #         cnts[num] += 1
        
    #     return ans % MOD

# @lc code=end

