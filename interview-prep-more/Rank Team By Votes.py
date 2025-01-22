class Solution:    
    def rankTeams(self, votes: List[str]) -> str:
        d = {}

        for vote in votes:
            for i, char in enumerate(vote):
                if char not in d:
                    d[char] = [0] * len(vote)
                d[char][i] += 1

        voted_names = sorted(d.keys())
        return "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))

"""
class Solution:   
    def rankTeams(self, votes: List[str]) -> str:
    num_votes, num_teams = len(votes), len(votes[0])
    
    ranks = { team: [num_votes]*num_teams for team in votes[0] }

    for i in range(num_teams):
        for vote in votes:
            team = vote[i]
            ranks[team][i] -= 1

    teams_sorted = sorted(ranks.items(), key=lambda x: (x[1], x[0]))
    
    ret = [team[0] for team in teams_sorted]
    return "".join(ret)

"""
