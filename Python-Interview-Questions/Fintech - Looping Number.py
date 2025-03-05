"""
def is_looping(n):
    def next_number(num):
        nxt = 0
        while num > 0:
            cur = num % 10
            nxt += cur**2
            num //= 10
        return nxt
    
    tortoise = n
    hare = next_number(n)

    while tortoise != hare:
        
        tortoise = next_number(tortoise)
      
        hare = next_number(next_number(hare))
    
    return hare != 1  
"""
 
def is_looping(n):
    def next_number(num):
        nxt = 0
        while num > 0:
            cur = num % 10
            nxt += cur**2
            num //= 10
        return nxt
    
    visited = set()
    while n != 1:
        if n in visited:
            return True
        visited.add(n)
        n = next_number(n)
    return False
    
"""    
def next_number(num):
    nxt = 0
    # Convert the number to a string
    str_num = str(num)
    for d in str_num:
        # Convert the digit back to an integer and add its square
        nxt += int(d)**2
    return nxt
"""
