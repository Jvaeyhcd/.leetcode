/*
 * @lc app=leetcode.cn id=870 lang=cpp
 *
 * [870] 优势洗牌
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> advantageCount(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        int n = nums1.size(), ids[n];
        vector<int> ans(n);
        iota(ids, ids + n, 0);
        sort(ids, ids + n, [&](int i, int j) {
            return nums2[i] < nums2[j];
        });
        int l = 0, r = n - 1;
        for (int x: nums1) {
            if (x > nums2[ids[l]]) {
                ans[ids[l]] = x;
                l += 1;
            } else {
                ans[ids[r]] = x;
                r -= 1;
            }
        }
        return ans;
    }
};
// @lc code=end

