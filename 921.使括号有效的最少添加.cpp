/*
 * @lc app=leetcode.cn id=921 lang=cpp
 *
 * [921] 使括号有效的最少添加
 */
#include<bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int minAddToMakeValid(string s) {
        int ans = 0, cnt = 0;
        for (char c: s) {
            if (c == '(') {
                cnt += 1;
            } else if (cnt > 0) {
                cnt -= 1;
            } else {
                ans += 1;
            }
        }
        return ans + cnt;
    }
};
// @lc code=end

