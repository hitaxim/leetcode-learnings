def max_satisfaction(expectations, cards):
    expectations.sort()
    cards.sort()
    
    satisfied_count = 0
    expectation_index = 0  
    card_index = 0        
    
    while expectation_index < len(expectations) and card_index < len(cards):
       
        if cards[card_index] >= expectations[expectation_index]:
          
            satisfied_count += 1
            expectation_index += 1
   
        card_index += 1
    
    return satisfied_count
