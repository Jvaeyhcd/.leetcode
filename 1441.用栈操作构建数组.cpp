/*
 * @lc app=leetcode.cn id=1441 lang=cpp
 *
 * [1441] 用栈操作构建数组
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> ans;
        int num = 0;
        for (int i: target) {
            ans.push_back("Push");
            for (int j = 0; j < i - num - 1; j++) {
                ans.push_back("Pop");
                ans.push_back("Push");
            }
            num = i;
        }
        return ans;
    }
};
// @lc code=end

