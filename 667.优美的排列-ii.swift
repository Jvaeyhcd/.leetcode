/*
 * @lc app=leetcode.cn id=667 lang=swift
 *
 * [667] 优美的排列 II
 */

// @lc code=start
class Solution {
    func constructArray(_ n: Int, _ k: Int) -> [Int] {
        var ans: [Int] = [Int]()
        var l = 1
        var r = k + 1
        ans.append(l)
        while l < r {
            if ans.last == l {
                ans.append(r)
                l += 1
            } else {
                ans.append(l)
                r -= 1
            }
        }
        for i in 1...n {
            if !ans.contains(i) {
                ans.append(i)
            }
        }
        return ans
    }
}
// @lc code=end

var solution = Solution()
var n = 3
var k = 2
print(solution.constructArray(n, k))
