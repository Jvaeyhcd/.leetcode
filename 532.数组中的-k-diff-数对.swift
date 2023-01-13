/*
 * @lc app=leetcode.cn id=532 lang=swift
 *
 * [532] 数组中的 k-diff 数对
 */

// @lc code=start
class Solution {
    func findPairs(_ nums: [Int], _ k: Int) -> Int {
        var cntA: [Int: Int] = [Int: Int]()
        for num in nums {
            if let v = cntA[num] {
                cntA[num] = v + 1
            } else {
                cntA[num] = 1
            }
        }
        
        var ans = 0
        for num in cntA.keys {
            if let cnt1 = cntA[num + k] {
                if k != 0 || (k == 0 && cnt1 > 1) {
                    ans += 1
                }
            }
            if let cnt2 = cntA[num - k] {
                if k != 0 || (k == 0 && cnt2 > 1) {
                    ans += 1
                }
            }
        }
        return ans / 2
    }
}
// @lc code=end

let solution = Solution()
var nums = [3, 1, 4, 1, 5]
var k = 2
nums = [1, 2, 3, 4, 5]
k = 1
// nums = [1, 3, 1, 5, 4]
// k = 0
print(solution.findPairs(nums, k))