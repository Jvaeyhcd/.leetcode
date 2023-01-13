/*
 * @lc app=leetcode.cn id=809 lang=cpp
 *
 * [809] 情感丰富的文字
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int expressiveWords(string s, vector<string>& words) {
        int ans = 0;
        for (string word: words) {
            if (expand(s, word)) ans += 1;
        }
        return ans;
    }

private:
    bool expand(string s, string t) {
        int i = 0, j = 0;
        while (i < s.size() && j < t.size()) {
            if (s[i] != t[j]) return false;
            char ch = s[i];
            int cnti = 0;
            while (i < s.size() && s[i] == ch) {
                cnti += 1; i += 1;
            }
            int cntj = 0;
            while (j < t.size() && t[j] == ch) {
                cntj += 1; j += 1;
            }
            if (cnti < cntj) return false;
            if (cnti != cntj && cnti < 3) return false;
        }
        return i == s.size() && j == t.size();
    }
};

// @lc code=end

