#
# @lc app=leetcode.cn id=726 lang=python
#
# [726] 原子的数量
#

# @lc code=start
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        # 元素个数哈希表
        cnts = collections.defaultdict(int)
        # 当前层乘数的基数
        mul = 1
        # 迭代中的乘数
        muls = []
        # 个数
        num = 0
        # 个数的10进制位数
        num_count = 0
        # 元素原子
        atom = ''
        for c in formula[::-1]:
            if c == ')':
                # 如果当前统计有数字，乘的基数要叠加
                if num:
                    mul *= num
                    muls.append(num)
                    num = num_count = 0
                else:
                    muls.append(1)
            elif c == '(':
                # 去掉上一个乘数
                mul //= muls.pop()
            elif c.isdigit():
                num += int(c) * (10 ** num_count)
                num_count += 1
            elif c.islower():
                atom += c
            else:
                atom += c
                # 更新元素时需要考虑乘的基数
                if num:
                    cnts[atom[::-1]] += mul * num
                else:
                    cnts[atom[::-1]] += mul
                atom = ''
                num = num_count = 0
        
        return ''.join([(name + str(cnts[name])) if cnts[name] > 1 else name for name in sorted(cnts.keys())])

# @lc code=end

