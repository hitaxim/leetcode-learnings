
class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.feed = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.appendleft((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        return [tweetId for user, tweetId in self.feed if userId == user or user in self.follows[userId]][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

"""
class Twitter:

    def __init__(self):
        self.time=0
        self.followmap=defaultdict(set)
        self.tweet=defaultdict(list)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.time,tweetId])
        self.time-=1
    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        heap=[]
        self.followmap[userId].add(userId)
        for id in self.followmap[userId]:
            if id in self.tweet:
                index=len(self.tweet[id])-1
                time,tweet=self.tweet[id][index]
                heapq.heappush(heap,[time,tweet,id,index-1])
        while heap and len(res)<10:
            time,tweet,id,index=heapq.heappop(heap)
            res.append(tweet)
            if index>=0:
                time,tweet=self.tweet[id][index]
                heapq.heappush(heap,[time,tweet,id,index-1])
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)


"""

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
