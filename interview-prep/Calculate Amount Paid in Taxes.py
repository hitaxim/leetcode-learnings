class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        last_upper = 0
        for b in brackets: 
            rate = b[1]/100
            upper = min(b[0], income)
            tax += (upper - last_upper) * rate
            last_upper = upper 
        return tax
