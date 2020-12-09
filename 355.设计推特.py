'''
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人
（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发
出的。推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户

示例:
Twitter twitter = new Twitter();

// 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
twitter.postTweet(1, 5);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
twitter.getNewsFeed(1);

// 用户1关注了用户2.
twitter.follow(1, 2);

// 用户2发送了一个新推文 (推文id = 6).
twitter.postTweet(2, 6);

// 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
// 推文id6应当在推文id5之前，因为它是在5之后发送的.
twitter.getNewsFeed(1);

// 用户1取消关注了用户2.
twitter.unfollow(1, 2);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
// 因为用户1已经不再关注用户2.
twitter.getNewsFeed(1);
'''
from typing import List


class Twitter:

    def __init__(self):
        self.allpost = []
        self.userfollow = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.allpost.append([userId, tweetId])
        if userId not in self.userfollow:
            self.userfollow[userId] = [userId]

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        if userId not in self.userfollow:
            self.userfollow[userId] = [userId]
        n = len(self.allpost)
        k = 10
        cur = n-1
        while cur >= 0 and k > 0:
            if self.allpost[cur][0] in self.userfollow[userId]:
                result.append(self.allpost[cur][1])
                k -= 1
            cur -= 1
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userfollow:
            self.userfollow[followerId] = [followerId]
        if followeeId not in self.userfollow[followerId]:
            self.userfollow[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userfollow:
            self.userfollow[followerId] = [followerId]
        if followeeId in self.userfollow[followerId] and followeeId != followerId:
            self.userfollow[followerId].remove(followeeId)


twitter = Twitter()
twitter.postTweet(1, 5)
twitter.unfollow(1, 1)
print(twitter.getNewsFeed(1))
# twitter.unfollow(1, 2)
# print(twitter.getNewsFeed(1))
