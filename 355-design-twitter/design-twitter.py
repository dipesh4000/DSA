from typing import List


class Twitter:

    def __init__(self):
        self.user = {}
        self.posts = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user:
            self.user[userId] = [userId]

        self.posts.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user:
            return []

        flw = self.user[userId]
        feed = []

        for i in range(len(self.posts) - 1, -1, -1):
            post = self.posts[i]

            if post[0] in flw:
                feed.append(post[1])

            if len(feed) >= 10:
                break

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user:
            self.user[followerId] = [followerId]

        if followeeId not in self.user[followerId]:
            self.user[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId in self.user and followeeId in self.user[followerId]:
            self.user[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
