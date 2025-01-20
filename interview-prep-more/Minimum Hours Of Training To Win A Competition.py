class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        energyLose = sum(energy)

        availableEnergy = max(0, energyLose - initialEnergy + 1)
        
        experienceEarn = 0
        
        for exp in experience:
            if initialExperience <= exp:
                experienceEarn += (exp - initialExperience +1)
                initialExperience += (exp - initialExperience +1)
            initialExperience += exp
        
        return availableEnergy + experienceEarn

