class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lowest = 0
        highest = len(s)
        perm = []
        for char in s:
            if char == 'I':
                perm.append(lowest)
                lowest+=1
            else:
                perm.append(highest)
                highest -= 1
        perm.append((lowest+highest)//2)
        return perm
