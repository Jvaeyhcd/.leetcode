#
# @lc app=leetcode.cn id=838 lang=python3
#
# [838] 推多米诺
#

# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        l, r = -1, -1
        last = ''
        arr = list(dominoes)
        segment = set()
        left, right = [], []
        for i, ch in enumerate(dominoes):
            if last != ch:
                if ch == 'L':
                    r = i
                if last == 'R':
                    l = i - 1
                if l < r and l != -1 and r != -1 and (l, r) not in segment:
                    segment.add((l, r))
                if ch == 'L':
                    l = -1
            last = ch
            if ch == 'L':
                left.append(i)
            elif ch == 'R':
                right.append(i)
        visited = set()
        for l, r in segment:
            while l < r:
                visited.add(l)
                visited.add(r)
                arr[l] = 'R'
                arr[r] = 'L'
                l += 1
                r -= 1
            if l == r:
                arr[l] = '.'
                visited.add(l)
        # print(segment)
        for l in left:
            for i in range(l - 1, -1, -1):
                if i in visited:
                    break
                arr[i] = 'L'
                visited.add(i)
        for r in right:
            for i in range(r, n):
                if i in visited:
                    break
                arr[i] = 'R'
                visited.add(i)
        ans = ''.join(arr)
        return ans

# @lc code=end

solution = Solution()
dominoes = "RR.L"
# dominoes = ".LL.RRR...LLLR..L.."
# dominoes = ".L.R...LR..L.."
dominoes = "L.....RR.RL.....L.R."
print(solution.pushDominoes(dominoes))
