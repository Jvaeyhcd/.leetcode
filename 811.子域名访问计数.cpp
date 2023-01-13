/*
 * @lc app=leetcode.cn id=811 lang=cpp
 *
 * [811] 子域名访问计数
 */
#include <bits/stdc++.h>
#include <string>
using namespace std;
// @lc code=start

vector<string> split(const string& str, const string& delim) {
    vector<string> res;
    if ("" == str) {
        return res;
    }
    char *strs = new char[str.length() + 1];
    strcpy(strs, str.c_str());

    char *d = new char[delim.length() + 1];
    strcpy(d, delim.c_str());

    char *p = strtok(strs, d);
    while (p) {
        string s = p;
        res.push_back(s);
        p = strtok(NULL, d);
    }
    return res;
}

class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        vector<string> res;
        map<string, int> cnts;
        for (string d: cpdomains) {
            int space = d.find(' ');
            int cnt = stoi(d.substr(0, space));
            string domain = d.substr(space + 1);
            cnts[domain] += cnt;
            for (int i = 0; i < domain.size(); i++) {
                if (domain[i] == '.') {
                    string subdomain = domain.substr(i + 1);
                    cnts[subdomain] += cnt;
                }
            }
        }
        for (auto &&[subdomain, cnt]: cnts) {
            res.emplace_back(to_string(cnt) + " " + subdomain);
        }
        return res;
    }
};
// @lc code=end

