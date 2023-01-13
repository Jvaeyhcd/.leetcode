/*
 * @lc app=leetcode.cn id=2027 lang=cpp
 *
 * [2027] 转换字符串的最少操作次数
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int minimumMoves(string s) {
        int covered = -1, ans = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == 'X' && i > covered) {
                ans++;
                covered = i + 2;
            }
        }
        return ans;
    }
};
// @lc code=end

