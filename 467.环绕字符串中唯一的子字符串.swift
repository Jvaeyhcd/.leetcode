/*
 * @lc app=leetcode.cn id=467 lang=swift
 *
 * [467] 环绕字符串中唯一的子字符串
 */

// @lc code=start
class Solution {
    func findSubstringInWraproundString(_ p: String) -> Int {
        var arr = [Int]()
        let aassic = Int(Character("a").asciiValue!)
        for c in p.unicodeScalars {
            arr.append(Int(c.value) - aassic)
        }
        let circle = 26
        var dp = [Int](repeating: 0, count: 26)
        var k = 0
        for i in 0..<arr.count {
            if i > 0 && (arr[i - 1] + 1) % circle == arr[i] {
                k += 1
            } else {
                k = 1
            }
            dp[arr[i]] = max(dp[arr[i]], k)
        }
        var ans = 0
        for n in dp {
            ans += n
        }
        return ans
    }
}
// @lc code=end

var solution = Solution()
var p = "zab"
p = "cac"
print(solution.findSubstringInWraproundString(p))