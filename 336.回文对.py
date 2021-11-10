#
# @lc app=leetcode.cn id=336 lang=python
#
# [336] 回文对
#

# @lc code=start
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        

class TireNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Tire(object):
    # 初始化字典树
    def __init__(self):
        self.root = TireNode()
    
    # 插入到字段数中
    def insert(self, word):
        current = self.root
        for c in word:
            if not current.children.get(c):
                current.children[c] = TireNode()
            current = current.children[c]
        current.is_word = True
    
    # 查找完整的单词
    def search(self, word):
        current = self.root
        for c in word:
            current = current.children.get(c)
            if not current:
                return False
        return current.is_word

    # 是否以prefix前缀开始
    def start_with(self, prefix):
        current = self.root
        for c in prefix:
            current = current.children.get(c):
            if not current:
                return False
        return True

# @lc code=end

