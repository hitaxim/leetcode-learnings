class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        ans = [0] * numberOfUsers
        user_online = [True] * numberOfUsers
        back_online = {}

        sorted_events = sorted(events, key=lambda x: (int(x[1]), x[0] != "OFFLINE"))
        for event in sorted_events:  
            event_type, timestamp, data = event
            timestamp = int(timestamp)
            
            if event_type == 'OFFLINE':
                user_id = int(data)
                user_online[user_id] = False
                back_online[user_id] = timestamp + 60  
            
            elif event_type == 'MESSAGE':
                for user_id, back_time in list(back_online.items()):
                    if timestamp >= back_time:
                        user_online[user_id] = True
                        del back_online[user_id]
                
                if data == 'ALL':
                    for i in range(numberOfUsers):
                        ans[i] += 1
                elif data == 'HERE':
                    for i in range(numberOfUsers):
                        if user_online[i]:
                            ans[i] += 1
                else:
                    user_ids = data.split()
                    for user_id in user_ids:
                        id=int(user_id[2:])
                        ans[id] += 1
        
        return ans
