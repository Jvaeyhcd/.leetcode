#
# @lc app=leetcode.cn id=722 lang=python3
#
# [722] 删除注释
#

# @lc code=start
from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        # 前面有多行注释的标识
        flag1 = False
        for line in source:
            # 前面有单行注释的标识
            flag2 = False
            l = len(line)
            i = 0
            tmp = '' if not flag1 else tmp
            while i < l:
                # print(line[i])
                if i + 1 < l and line[i] == '/' and line[i + 1] == '*':
                    # 注释开始标识
                    i += (1 if flag1 else 2)
                    if not flag2:
                        flag1 = True
                    continue
                elif i + 1 < l and line[i] == '*' and line[i + 1] == '/':
                    if flag1:
                        # 注释结束标识
                        i += 2
                        flag1 = False
                        flag2 = False
                        continue
                elif i + 1 < l and line[i] == line[i + 1] == '/':
                    # 单行注释
                    flag2 = True
                    i += 2
                    continue
                if not flag1 and not flag2:
                    tmp += line[i]
                i += 1
            if tmp != '' and not flag1: 
                ans.append(tmp)

        return ans
                
                
# @lc code=end

s = Solution()
# source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
# source = ["a/*comment", "line", "more_comment*/b"]
# source = ["main() {", "/* here is commments", "  // still comments */adadda", "   double s = 33;", "   cout << s;", "}"]
# source = ["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]
source = ["a//*b/*/c","blank","d/*/e/*/f"]
print(s.removeComments(source))