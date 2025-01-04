class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        curr_five, curr_ten = 0, 0
        for change in bills:
            if change == 5:
                curr_five += 1
            elif change == 10:
                curr_five -= 1
                curr_ten += 1
            elif curr_ten > 0:
                curr_ten -= 1
                curr_five -= 1
            else: 
                curr_five -= 3

            if curr_five < 0:
                return False 

        return True 
    
