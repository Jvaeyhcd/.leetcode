#
# @lc app=leetcode.cn id=752 lang=python
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        forword_seen = set()
        backword_seen = set()
        deadends = set(deadends)

        source = '0000'
        if source in deadends:
            return -1
        if source == target:
            return 0
        
        forword_queue = collections.deque([source])
        forword_seen.add(source)
        forword_step = 0

        backword_queue = collections.deque([target])
        backword_seen.add(target)
        backword_step = 0

        while forword_queue and backword_queue:

            # 从初始订单到目标顶点
            forword_len = len(forword_queue)
            for _ in range(forword_len):
                node = forword_queue.popleft()
                if node in backword_seen:
                    return forword_step + backword_step
                for i in range(4):
                    for d in range(-1, 2, 2):
                        digit = str((int(node[i]) + d + 10) % 10)
                        new_node = node[:i] + str(digit) + node[i+1:]

                        if new_node not in forword_seen and new_node not in deadends:
                            forword_queue.append(new_node)
                            forword_seen.add(new_node)
            forword_step += 1

            # 从目标顶点到初始顶点
            backword_len = len(backword_queue)
            for _ in range(backword_len):
                node = backword_queue.popleft()
                if node in forword_seen:
                    return forword_step + backword_step
                for i in range(4):
                    for d in range(-1, 2, 2):
                        digit = str((int(node[i]) + d + 10) % 10)
                        new_node = node[:i] + str(digit) + node[i+1:]

                        if new_node not in backword_seen and new_node not in deadends:
                            backword_queue.append(new_node)
                            backword_seen.add(new_node)
            backword_step += 1

        return -1

# @lc code=end

