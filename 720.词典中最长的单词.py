#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
import collections
from typing import List


class TireNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False


class Tire:
    def __init__(self):
        self.root = TireNode()

    
    def insert(self, word: str):
        node = self.root
        for ch in word:
            child = node.children.get(ch)
            if not child:
                node.children[ch] = TireNode()
            node = node.children[ch]
        node.isWord = True


    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if not node or not node.isWord:
                return False
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        tire = Tire()
        for word in words:
            tire.insert(word)

        ans = ''
        for word in words:
            if tire.search(word) and (len(ans) < len(word) or (len(ans) == len(word) and word < ans)):
                ans = word
        return ans
# @lc code=end

