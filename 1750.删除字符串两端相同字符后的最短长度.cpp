/*
 * @lc app=leetcode.cn id=1750 lang=cpp
 *
 * [1750] 删除字符串两端相同字符后的最短长度
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int minimumLength(string s) {
        int l = 0, r = s.size() - 1;
        while (l < r && s[l] == s[r]) {
            char c = s[l];
            while (l <= r && s[l] == c) l += 1;
            while (r >= l && s[r] == c) r -= 1;
        }
        return r - l + 1;
    }
};
// @lc code=end

