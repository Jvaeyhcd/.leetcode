#
# @lc app=leetcode.cn id=2115 lang=python3
#
# [2115] 从给定原材料中找到所有可以做出的菜
#

# @lc code=start
import collections
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        g = collections.defaultdict(list)
        indeg = collections.defaultdict(int)
        
        for i, u in enumerate(recipes):
            for v in ingredients[i]:
                g[v].append(u)
            indeg[u] = len(ingredients[i])
        
        ans = []
        q = [u for u in supplies]
        while q:
            u = q.pop(0)
            for v in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    ans.append(v)
                    q.append(v)
        return ans

# @lc code=end

solution = Solution()

recipes = ["bread"]
ingredients = [["yeast","flour"]]
supplies = ["yeast"]

# recipes = ["bread","sandwich","burger"]
# ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
# supplies = ["yeast","flour","meat"]

# recipes = ["bread","sandwich"]
# ingredients = [["yeast","flour"],["bread","meat"]]
# supplies = ["yeast","flour","meat"]

# recipes = ["ju","fzjnm","x","e","zpmcz","h","q"]
# ingredients = [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]]
# supplies = ["f","hveml","cpivl","d"]

# recipes = ["xevvq","izcad","p","we","bxgnm","vpio","i","hjvu","igi","anp","tokfq","z","kwdmb","g","qb","q","b","hthy"]
# ingredients = [["wbjr"],["otr","fzr","g"],["fzr","wi","otr","xgp","wbjr","igi","b"],["fzr","xgp","wi","otr","tokfq","izcad","igi","xevvq","i","anp"],["wi","xgp","wbjr"],["wbjr","bxgnm","i","b","hjvu","izcad","igi","z","g"],["xgp","otr","wbjr"],["wbjr","otr"],["wbjr","otr","fzr","wi","xgp","hjvu","tokfq","z","kwdmb"],["xgp","wi","wbjr","bxgnm","izcad","p","xevvq"],["bxgnm"],["wi","fzr","otr","wbjr"],["wbjr","wi","fzr","xgp","otr","g","b","p"],["otr","fzr","xgp","wbjr"],["xgp","wbjr","q","vpio","tokfq","we"],["wbjr","wi","xgp","we"],["wbjr"],["wi"]]
# supplies = ["wi","otr","wbjr","fzr","xgp"]

recipes = ["fe","nvvj","kps","ik","gd","gjpz","cff","ljb","ybxsh","vtu","htsn","jwwxz","znoem","h","mlg","ggd","bkinz","pzjna","pxum"]
ingredients = [["zqg"],["zqg"],["t"],["zqg"],["bkinz","ggd","ljb","ybxsh","nvvj","pzjna","cff"],["kps","nvvj","pxum","ik","cff","ybxsh","h"],["yyym"],["zqg"],["htsn","vtu"],["kfukc"],["zqg"],["zqg"],["a"],["zqg","gd","ybxsh","ggd","ljb"],["ybxsh","pxum","h","bkinz"],["zqg"],["zqg"],["mu"],["zqg"]]
supplies = ["zqg"]

print(solution.findAllRecipes(recipes, ingredients, supplies))