'''
author: noc
time：2020年4月13日
url：https://leetcode-cn.com/problems/design-twitter/
'''
'''
此题考查难度不大，重点是在检查传递过来的参数合法性，本人在这里踩过无数的坑，包括，用户是否存在，用户取关了根本没有关注的人，获取了根本没有的用户发的不存在的文章。
总之，记住在任何的项目代码里，一定要慎重慎重的检查参数是否合法，这里的合法指的是参数在基本数据类型合法的情况下， 业务逻辑不合法。
'''
class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.getFollow = dict()  # 存放关注的人的字典
        self.Tweets = []         # 存放推特信息
        self.tweetNums = 0       # 存放推特的数量

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.Tweets.append((userId, tweetId))
        self.tweetNums += 1
        if userId not in self.getFollow:    # 新用户初始化关注列表. 初始为空
            self.getFollow[userId] = []

    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.getFollow.keys():     # 此用户压根没有发过推特
            return
        ret = []    # 保存文章
        # followUserId = []
        nums = 0
        for i in range(self.tweetNums - 1, - 1, -1):
            k, v = self.Tweets[i]
            if k == userId or k in self.getFollow[userId]:      # 如果这条推特是本人发的或者是本人所关注的人发的
                ret.append(v)
                nums += 1
            if nums == 10:  # 达到每次获取的数量
                break
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.getFollow.keys():     # 此用户未初始化关注列表
            self.getFollow[followerId] = []
            self.getFollow[followerId].append(followeeId)
        else:
            self.getFollow[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.getFollow.keys(): # 用户不存在
            return
        if followeeId not in self.getFollow[followerId]:  # 如果没有关注此人
            return
        else:   # 关注了的
            self.getFollow[followerId].remove(followeeId)

if __name__ == '__main__':
    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.postTweet(1, 3)
    twitter.postTweet(2, 6)
    print(twitter.tweetNums)
    twitter.follow(2, 1)
    print(twitter.getNewsFeed(2))
    twitter.unfollow(2, 1)
    print(twitter.getFollow)
    print(twitter.getNewsFeed(1))