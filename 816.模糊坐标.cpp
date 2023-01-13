/*
 * @lc app=leetcode.cn id=816 lang=cpp
 *
 * [816] 模糊坐标
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<string> ambiguousCoordinates(string s) {
        auto make = [](const int i, const int j, string s) {
            vector<string> ans;
            for (int d = 1; d < j - i + 1; d++) {
                string left = s.substr(i, d);
                string right = s.substr(i + d, j - i - d);
                if ((left[0] != '0' || left == "0") && (right == "" || right[right.size() - 1] != '0')) {
                    ans.push_back(left + (d < j - i ? "." : "") + right);
                }
            }
            return ans;
        };

        vector<string> ans;
        for (int i = 2; i < s.size() - 1; i++) {
            for (string left: make(1, i, s)) {
                for (string right: make(i, s.size() - 1, s)) {
                    ans.push_back("(" + left + ", " + right + ")");
                }
            }
        }
        return ans;
    }
};
// @lc code=end

