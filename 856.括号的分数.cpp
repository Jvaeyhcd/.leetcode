/*
 * @lc app=leetcode.cn id=856 lang=cpp
 *
 * [856] 括号的分数
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int scoreOfParentheses(string s) {
        stack<int> st;
        st.push(0);
        for (char c: s) {
            if (c == '(') {
                st.push(0);
            } else {
                int v = st.top();
                st.pop();
                st.top() += max(2 * v, 1);
            }
        }
        return st.top();
    }
};
// @lc code=end

