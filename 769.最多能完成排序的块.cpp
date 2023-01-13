/*
 * @lc app=leetcode.cn id=769 lang=cpp
 *
 * [769] 最多能完成排序的块
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int ans = 0, total = 0, sum = 0;
        for (int i = 0; i < arr.size(); i++) {
            total += i;
            sum += arr[i];
            if (total == sum) ans += 1;
        }
        return ans;
    }
};
// @lc code=end

