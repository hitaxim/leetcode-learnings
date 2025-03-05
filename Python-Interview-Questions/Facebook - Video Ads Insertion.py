def can_insert_ads(feed_items, n):
    inserted_ads = 0
    zeros = 0
    
    if feed_items[0] == 0:
        inserted_ads += 1

    for i in range(len(feed_items)):
        if feed_items[i] != 0:
           
            if zeros > 1:
                inserted_ads += (zeros - 1)
          
            if inserted_ads >= n:
                return True
            zeros = 0 
        else:
            zeros += 1  

  
    if feed_items[-1] == 0:
        inserted_ads += 1
   
    if zeros > 1:
        inserted_ads += (zeros - 1)

    if inserted_ads >= n:
        return True
    else:
        return False
        
 
