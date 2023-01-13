#
# @lc app=leetcode.cn id=648 lang=python3
#
# [648] 单词替换
#

# @lc code=start
from typing import List


class TrieNode:

    def __init__(self) -> None:
        self.is_word = False
        self.children = {}


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    
    def insert(self, word: str):
        node = self.root
        for c in word:
            child = node.children.get(c)
            if not child:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    
    def search_root(self, word: str) -> str:
        prev = None
        node = self.root
        ans = ''
        for c in word:
            prev = node
            node = node.children.get(c)
            if not node:
                break
            ans += c
            if node.is_word:
                return ans
        if prev and prev.is_word:
            return ans
        else:
            return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        trie = Trie()
        for w in dictionary:
            trie.insert(w)
        
        return ' '.join([trie.search_root(word) for word in words])

# @lc code=end

solution = Solution()
dictionary = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
print(solution.replaceWords(dictionary, sentence))