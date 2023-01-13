/*
 * @lc app=leetcode.cn id=895 lang=cpp
 *
 * [895] 最大频率栈
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class FreqStack {
public:
    unordered_map<int, vector<int>> group;
    unordered_map<int, int> cnts;
    int maxcnt;
    FreqStack() {
        maxcnt = 0;
    }
    
    void push(int val) {
        int cnt = cnts[val] + 1;
        cnts[val] = cnt;
        if (cnt > maxcnt) maxcnt = cnt;
        group[cnt].push_back(val);
    }
    
    int pop() {
        int x = group[maxcnt].back();
        group[maxcnt].pop_back();
        cnts[x] -= 1;
        if (group[maxcnt].size() == 0) {
            maxcnt -= 1;
        }
        return x;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */
// @lc code=end

