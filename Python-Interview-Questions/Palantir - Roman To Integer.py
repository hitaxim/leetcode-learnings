
def romanToInt(s):
    rom = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, 
        "M": 1000, "CM": 900, "CD": 400, "IV": 4, "IX": 9, 
        "XL": 40, "XC": 90
    }
    ans = 0
    i = 0
    
    while i < len(s):
        '''
        Check if the next two characters form 
        a valid pair in the dictionary
        '''
        if i + 1 < len(s) and s[i:i+2] in rom:
            ans += rom[s[i:i+2]]
            i += 2
        else:
            ans += rom[s[i]]
            i += 1
            
    return ans
