#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU 缓存
#

# @lc code=start
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyMap = dict()
        self.freqMap = dict()
        self.minFreq = 0


    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        node = self.keyMap[key]
        self.updateNode(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.keyMap:
            node = self.keyMap[key]
            node.value = value
            self.updateNode(node)
        else:
            if self.capacity == 0:
                return
            # 达到缓存上线，删除评论最小的节点
            if len(self.keyMap) == self.capacity:
                self.deleteMinFreqNode()
            node = Node(key, value, 1)
            self.updateNode(node, True)
            self.keyMap[key] = node


    # 更新节点，是否是新增
    def updateNode(self, node: 'Node', isNew=False):
        if isNew:
            self.minFreq = 1
            self.setFreqLinkedList(node)
        else:
            self.deleteNode(node)
            node.freq += 1
            self.setFreqLinkedList(node)
            if self.minFreq not in self.freqMap:
                self.minFreq += 1
    

    # 从频率链表中删除指定节点
    def deleteNode(self, node: 'Node'):
        if node.freq not in self.freqMap:
            return
        linkedList = self.freqMap[node.freq]
        linkedList.delete(node)
        if linkedList.isEmpty():
            self.freqMap.pop(node.freq)


    # 删除频率最低的节点
    def deleteMinFreqNode(self):
        linkedList = self.freqMap[self.minFreq]
        node = linkedList.getLast()
        linkedList.delete(node)
        self.keyMap.pop(node.key)
        if linkedList.isEmpty():
            self.freqMap.pop(node.freq)


    # 将节点设置到对应频率的LinkedList中去
    def setFreqLinkedList(self, node: 'Node'):
        if node.freq not in self.freqMap:
            self.freqMap[node.freq] = DLinkedList()
        linkedList = self.freqMap[node.freq]
        linkedList.insertFirst(node)


class Node:
    def __init__(self, key=None, value=None, freq=0) -> None:
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    
    def insertFirst(self, node: 'Node'):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head


    def delete(self, node: 'Node'):
        if self.head.next == self.tail:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    
    def getLast(self) -> Node:
        if self.head.next == self.tail:
            return None
        return self.tail.prev


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

mp = {11: 1, 33: 3}
mp.pop(11)
print(mp)