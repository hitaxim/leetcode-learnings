def total_letters(N):
    base_word_count = {
        1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 
        7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 
        12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 
        17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 
        40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 
        90: 6
    }
    
    def get_count(num):
        count = 0
        if num >= 1000:
        	# "thousand" has 8 letters
            count += (base_word_count[num // 1000] + 8)  
            num %= 1000

        if num >= 100:
        	# "hundred" has 7 letters
            count += base_word_count[num // 100] + 7  
            num %= 100

        if num > 0 and count > 0:
            count += 3  # "and" has 3 letters

        if num >= 20:
            count += base_word_count[num // 10 * 10]
            num %= 10

        if num > 0:
            count += base_word_count[num]
            
        return count
    
    ans = 0
    for num in range(1, N + 1):
        ans += get_count(num)
    
    return ans   
