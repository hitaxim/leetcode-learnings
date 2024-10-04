class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        len_s = len(skill)
        if len_s == 2:
            return skill[0] * skill[1]

        skill.sort()
        team_skill = skill[0] + skill[-1]
        chem = skill[0] * skill[-1]

        for i in range(1, len_s // 2):
            if skill[i] + skill[-i-1] != team_skill:
                return -1
            chem += skill[i] * skill[-1 - i]
        
        return chem
"""
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        targetSkill = skill[0]+skill[-1]

        l = 0
        r = len(skill) -1
        res = 0
        while l < r:
            if skill[l]+skill[r] == targetSkill:
                res += skill[l]*skill[r]
                l+=1
                r-=1
            else:
                return -1
        return res
"""
