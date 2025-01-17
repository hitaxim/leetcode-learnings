from collections import deque, Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q = deque([id])
        visited = {id}

        for _ in range(level):
            for _ in range(len(q)):
                person = q.popleft()
                for friend in friends[person]:
                    if friend not in visited:
                        visited.add(friend)
                        q.append(friend)
        
        video_count = Counter(video for person in q for video in watchedVideos[person])
        return sorted(video_count.keys(), key = lambda x: (video_count[x], x))

       
