/*
 * @lc app=leetcode.cn id=719 lang=swift
 *
 * [719] 找出第 k 小的距离对
 */

// @lc code=start
class Solution {
    func smallestDistancePair(_ nums: [Int], _ k: Int) -> Int {
        var arr = nums
        arr.sort(by:<)
        
        func possible(_ guess: Int) -> Bool {
            var count = 0
            var left = 0
            for right in 0..<arr.count {
                while arr[right] - arr[left] > guess {
                    left += 1
                }
                count += right - left
            }
            return count >= k
        }

        var lo = 0
        var hi = arr[arr.count - 1] - arr[0]
        while lo < hi {
            let mid = (lo + hi) / 2
            if possible(mid) {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        return lo
    }
}
// @lc code=end

var solution = Solution()
var nums = [1,3,1,2,3,4,5,6]
var k = 1
nums = [1,1,1]
k = 2
nums = [1,6,1]
k = 3
nums = [62,100,4]
k = 2
print(solution.smallestDistancePair(nums, k))