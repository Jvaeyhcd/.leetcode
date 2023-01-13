#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
from typing import List
import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        self.successors = collections.defaultdict(set)

        def bfs():
            found = False
            word_set = set(wordList)
            queue = collections.deque([beginWord])
            visited = set([beginWord])

            # 下一层已访问的点
            next_level_visited = set()
            while queue:
                for _ in range(len(queue)):
                    current = queue.popleft()
                    # 当前单词的字符数组
                    chars = list(current)
                    for i in range(len(chars)):
                        origin = chars[i]
                        for j in range(26):
                            chars[i] = chr(ord('a') + j)
                            next = ''.join(chars)

                            if next in word_set and next not in visited:
                                if next == endWord:
                                    found = True
                                if next not in next_level_visited:
                                    next_level_visited.add(next)
                                    queue.append(next)
                                self.successors[current].add(next)
                        chars[i] = origin
                if found:
                    break
                visited |= next_level_visited
                next_level_visited.clear()

            return found
        
        self.ans = []
        def dfs(begin: str, end: str, path: List[str]):
            if begin == end:
                self.ans.append(path[:])
                return
            if begin not in self.successors:
                return
            for next in self.successors[begin]:
                path.append(next)
                dfs(next, end, path)
                path.pop()

        
        if not bfs():
            return []
        dfs(beginWord, endWord, [beginWord])
        return self.ans

# @lc code=end

s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(s.findLadders(beginWord, endWord, wordList))