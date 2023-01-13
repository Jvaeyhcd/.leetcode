/*
 * @lc app=leetcode.cn id=1106 lang=cpp
 *
 * [1106] 解析布尔表达式
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    bool parseBoolExpr(string expression) {
        stack<char> st;
        for (char c: expression) {
            if (c == ',') continue;
            if (c != ')') {
                st.push(c);
                continue;
            }
            int t = 0, f = 0;
            while (!st.empty() && st.top() != '(') {
                if (st.top() == 'f') {
                    f += 1;
                } else {
                    t += 1;
                }
                st.pop();
            }
            st.pop();
            char op = st.top(); st.pop();
            if (op == '!') {
                st.push(f == 1 ? 't' : 'f');
            } else if (op == '&') {
                st.push(f == 0 ? 't' : 'f');
            } else if (op == '|') {
                st.push(t != 0 ? 't' : 'f');
            }
        }
        return st.top() == 't';
    }
};
// @lc code=end

