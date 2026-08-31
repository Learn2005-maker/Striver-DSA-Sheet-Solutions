class Twitter:

    def __init__(self):
        self.tweets = []  # (time,userId,tweetId)
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((self.time, userId, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int):
        feed = []
        followers = self.following.get(userId, set())
        followers.add(userId)

        for t, uid, tid in reversed(self.tweets):
            if uid in followers:
                feed.append(tid)
            if len(feed) == 10:
                break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        # only one follower must count only ones we use set()
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()

obj.postTweet(1, 101)

print(obj.getNewsFeed(1))
obj.postTweet(2, 102)

obj.follow(1, 2)
print(obj.getNewsFeed(1))

obj.unfollow(1, 2)
print(obj.getNewsFeed(1))






# tweets:
# [
#     (0, 1, 101),
#     (1, 2, 102),
#     (2, 1, 103)
# ]

# following:
# {
#     1: {2, 3},
#     2: {1}
# }


"""Complexity Analysis

Let:

T = total number of tweets
F = number of users followed by userId
postTweet()
self.tweets.append(...)

Time: O(1)

Space: O(T)

follow()

Set insertion:

Time: O(1) average

Space: O(F)

unfollow()

Set deletion:

Time: O(1) average

getNewsFeed()

We scan tweets from newest to oldest:

for ... in reversed(self.tweets):

In the worst case, we may scan all T tweets.

Time: O(T)

Space: O(F) for the followers set operation, depending on implementation.
        """