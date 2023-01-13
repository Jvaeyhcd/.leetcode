/*
 * @lc app=leetcode.cn id=777 lang=cpp
 *
 * [777] 在LR字符串中交换相邻字符
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    bool canTransform(string start, string end) {
        auto s = start, e = end;
        s.erase(remove(s.begin(), s.end(), 'X'), s.end());
        e.erase(remove(e.begin(), e.end(), 'X'), e.end());
        if (s != e) return false;
        for (int i = 0, j = 0; i < start.length(); ++i) {
            if (start[i] == 'X') continue;
            while (end[j] == 'X') ++j;
            if (i != j && (start[i] == 'L') != (i > j)) return false;
            ++j;
        }
        return true;
    }
};
// @lc code=end

