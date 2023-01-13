/*
 * @lc app=leetcode.cn id=1800 lang=cpp
 *
 * [1800] 最大升序子数组和
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int n = nums.size(), l = 0;
        int res = 0;
        while (l < n) {
            int r = l, s = nums[l];
            while (r + 1 < n && nums[r] < nums[r + 1]) {
                r += 1;
                s += nums[r];
            }
            if (l == r) {
                l += 1;
            } else {
                l = r + 1;
            }
            res = max(res, s);
        }
        return res;
    }
};
// @lc code=end

int main() {
    Solution s = Solution();
    vector<int> nums = {10,20,30,5,10,50};
    int ans = s.maxAscendingSum(nums);
    cout << ans << endl;
    return 0;
}