/*
 * @lc app=leetcode.cn id=904 lang=cpp
 *
 * [904] 水果成篮
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int n = fruits.size();
        int l = 0, ans = 0, r = 0;
        set<int> s;
        map<int, int> cnts;
        s.insert(fruits[l]);
        for (int r = 0; r < n; r++) {
            int f = fruits[r];
            s.insert(f);
            cnts[f] += 1;
            while (s.size() > 2) {
                cnts[fruits[l]] -= 1;
                if (cnts[fruits[l]] == 0) {
                    s.erase(fruits[l]);
                }
                l += 1;
            }
            ans = max(r - l + 1, ans);
        }
        return ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution* solution = new Solution();
    vector<int> fruits = {0,1,2,2};
    cout << solution->totalFruit(fruits) << endl;
    return 0;
}
