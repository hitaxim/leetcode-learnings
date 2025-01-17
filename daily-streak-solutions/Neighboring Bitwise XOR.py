class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        for first in [0, 1]:
            original = first
            for result in derived[:-1]:
                original = original ^ result
            if original ^ first == derived[-1]:
                return True 
        return False
        
