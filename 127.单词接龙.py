#
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
#

# @lc code=start
class Solution(object):
    # 广度优先搜索
    # def ladderLength(self, beginWord, endWord, wordList):
    #     word_table = dict()
    #     edge = collections.defaultdict(list)
    #     self.node_num = 0

    #     def add_word(word):
    #         if word not in word_table:
    #             word_table[word] = self.node_num
    #             self.node_num += 1
        
    #     def add_edge(word):
    #         add_word(word)
    #         id1 = word_table[word]
    #         chars = list(word)
    #         for i in range(len(chars)):
    #             tmp = chars[i]
    #             chars[i] = '*'
    #             new_word = ''.join(chars)
    #             add_word(new_word)
    #             id2 = word_table[new_word]
    #             edge[id1].append(id2)
    #             edge[id2].append(id1)
    #             chars[i] = tmp

    #     for word in wordList:
    #         add_edge(word)

    #     add_edge(beginWord)
    #     if endWord not in word_table:
    #         return 0
        
    #     dis = [float('inf')] * self.node_num
    #     begin_id, end_id = word_table[beginWord], word_table[endWord]
    #     dis[begin_id] = 0
    #     que = collections.deque([begin_id])
    #     while que:
    #         x = que.popleft()
    #         if x == end_id:
    #             return dis[end_id] // 2 + 1
            
    #         for it in edge[x]:
    #             if dis[it] == float('inf'):
    #                 dis[it] = dis[x] + 1
    #                 que.append(it)
        
    #     return 0

    # 双向BFS
    def ladderLength(self, beginWord, endWord, wordList):
        word_table = dict()
        edge = collections.defaultdict(list)
        self.node_num = 0

        def add_word(word):
            if word not in word_table:
                word_table[word] = self.node_num
                self.node_num += 1
        
        def add_edge(word):
            add_word(word)
            id1 = word_table[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = '*'
                new_word = ''.join(chars)
                add_word(new_word)
                id2 = word_table[new_word]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        for word in wordList:
            add_edge(word)

        add_edge(beginWord)
        if endWord not in word_table:
            return 0
        
        dis_begin = [float("inf")] * self.node_num
        begin_id = word_table[beginWord]
        dis_begin[begin_id] = 0
        begin_queue = collections.deque([begin_id])

        dis_end = [float("inf")] * self.node_num
        end_id = word_table[endWord]
        dis_end[end_id] = 0
        end_queue = collections.deque([end_id])

        while begin_queue or end_queue:
            begin_size = len(begin_queue)
            for _ in range(begin_size):
                begin_node = begin_queue.popleft()
                if dis_end[begin_node] != float("inf"):
                    return (dis_begin[begin_node] + dis_end[begin_node]) // 2 + 1
                
                for it in edge[begin_node]:
                    if dis_begin[it] == float("inf"):
                        dis_begin[it] = dis_begin[begin_node] + 1
                        begin_queue.append(it)
            
            end_size = len(end_queue)
            for _ in range(end_size):
                end_node = end_queue.popleft()
                if dis_begin[end_node] != float("inf"):
                    return (dis_begin[end_node] + dis_end[end_node]) // 2 + 1
                
                for it in edge[end_node]:
                    if dis_end[it] == float("inf"):
                        dis_end[it] = dis_end[end_node] + 1
                        end_queue.append(it)
        
        return 0

# @lc code=end

