/*
 * @lc app=leetcode.cn id=1832 lang=cpp
 *
 * [1832] 判断句子是否为全字母句
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    bool checkIfPangram(string sentence) {
        set<char> s;
        for (char c: sentence) s.insert(c);
        return s.size() == 26;
    }
};
// @lc code=end

