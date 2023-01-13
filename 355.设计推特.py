#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#

# @lc code=start
import collections
from typing import List


class ListNode:
    def __init__(self, userId=0, tweetId=-1):
        self.userId = userId
        self.tweetId = tweetId
        self.next = None


class Twitter:

    def __init__(self):
        self.graph = collections.defaultdict(list)
        self.head = ListNode()


    def postTweet(self, userId: int, tweetId: int) -> None:
        node = ListNode(userId, tweetId)
        node.next = self.head.next
        self.head.next = node


    def getNewsFeed(self, userId: int) -> List[int]:
        friends = self.graph[userId] + [userId]
        ans = []
        cnt = 0
        cur = self.head.next
        while cur and cnt < 10:
            uid, tid = cur.userId, cur.tweetId
            if uid in friends:
                ans.append(tid)
                cnt += 1
            cur = cur.next
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.graph[followerId]:
            self.graph[followerId] = [followeeId]
        elif followeeId not in self.graph[followerId]:
            self.graph[followeeId].append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.graph[followerId]:
            for i, uid in enumerate(self.graph[followerId]):
                if uid == followeeId:
                    self.graph[followerId].pop(i)
                    break



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

