#
# @lc app=leetcode.cn id=706 lang=python
#
# [706] 设计哈希映射
#

# @lc code=start
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 1009


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        row, col = key / 1000, key % 1000
        self.map[row][col] = value


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        row, col = key / 1000, key % 1000
        return self.map[row][col]


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        row, col = key / 1000, key % 1000
        self.map[row][col] = -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

