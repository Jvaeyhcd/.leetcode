/*
 * @lc app=leetcode.cn id=1021 lang=swift
 *
 * [1021] 删除最外层的括号
 */

// @lc code=start

extension String {
    
    subscript(_ i: Int) -> Character {
        get {return self[index(startIndex, offsetBy: i)]}
    }
    
    subscript(_ indexs: ClosedRange<Int>) -> String {
        let beginIndex = index(startIndex, offsetBy: indexs.lowerBound)
        let endIndex = index(startIndex, offsetBy: indexs.upperBound)
        return String(self[beginIndex...endIndex])
    }
    
    subscript(_ indexs: Range<Int>) -> String {
        let beginIndex = index(startIndex, offsetBy: indexs.lowerBound)
        let endIndex = index(startIndex, offsetBy: indexs.upperBound)
        return String(self[beginIndex..<endIndex])
    }
    
    subscript(_ indexs: PartialRangeThrough<Int>) -> String {
        let endIndex = index(startIndex, offsetBy: indexs.upperBound)
        return String(self[startIndex...endIndex])
    }
    
    subscript(_ indexs: PartialRangeFrom<Int>) -> String {
        let beginIndex = index(startIndex, offsetBy: indexs.lowerBound)
        return String(self[beginIndex..<endIndex])
    }
    
    subscript(_ indexs: PartialRangeUpTo<Int>) -> String {
        let endIndex = index(startIndex, offsetBy: indexs.upperBound)
        return String(self[startIndex..<endIndex])
    }
}

class Solution {
    func removeOuterParentheses(_ s: String) -> String {
        var leftCount = 0
        var rightCount = 0
        let n = s.count
        var tmp = ""
        var ans = ""
        for i in 0..<n {
            let ch = s[i]
            if ch == "(" {
                leftCount += 1
            }
            if ch == ")" {
                rightCount += 1
            }
            tmp += String(ch)
            if leftCount == rightCount {
                ans += tmp[1..<tmp.count-1]
                tmp = ""
                leftCount = 0
                rightCount = 0
            }
        }
        return ans
    }
}
// @lc code=end

