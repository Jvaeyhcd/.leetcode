#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.word = ""
        self.is_word = False
    
    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ans = set()
        m, n = len(board), len(board[0])

        def dfs(cur, x, y):
            if board[x][y] not in cur.children:
                return
            
            ch = board[x][y]
            cur = cur.children[ch]
            if cur.word != "":
                ans.add(cur.word)
            
            board[x][y] = "#"
            for nx, ny in [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]:
                if 0 <= nx < m and 0 <= ny < n:
                    dfs(cur, nx, ny)
            board[x][y] = ch
        
        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)
        
        return list(ans)

# @lc code=end

