def coin_change(coins, target_amount):
    # Initialize the array with infinity
    min_coins = [float('inf')] * (target_amount + 1)
    min_coins[0] = 0  # Zero coins needed to make amount 0
    
    # Iterate over each coin
    for coin in coins:
        # Update min_coins for values >= coin
        for current_amount in range(coin, target_amount + 1):
            # Calculate the new number of coins
            potential_count = min_coins[current_amount - coin] + 1
            # Take the minimum of the current value or potential_count
            min_coins[current_amount] = min(min_coins[current_amount], potential_count)
    
    # Check if it's possible to construct the target amount
    if min_coins[target_amount] == float('inf'):
        return -1
    else:
        return min_coins[target_amount]
        
