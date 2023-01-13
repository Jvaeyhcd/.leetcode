#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.n = capacity
        self.mp = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.r = self.tail
        self.tail.l = self.head


    def delete(self, node: 'Node'):
        if node and node.l:
            left = node.l
            left.r = node.r
            node.r.l = left


    def refresh(self, node: 'Node'):
        self.delete(node)
        node.r = self.head.r
        node.l = self.head
        self.head.r.l = node
        self.head.r = node


    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self.refresh(node)
            return node.v
        return -1


    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.mp:
            node = self.mp[key]
            node.v = value
        else:
            if len(self.mp) == self.n:
                last = self.tail.l
                self.mp.pop(last.k)
                self.delete(last)
            node = Node(key, value)
            self.mp[key] = node
                
        self.refresh(node)


class Node:
    def __init__(self, k: int, v: int) -> None:
        self.k = k
        self.v = v
        self.l = None
        self.r = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

