WITH recent_transactions AS (
    SELECT 
        user_id,
        transaction_date,
        COUNT(product_id) AS purchase_count,
        RANK() OVER (PARTITION BY user_id ORDER BY transaction_date DESC) AS rank
    FROM user_transactions
    GROUP BY user_id, transaction_date
)
SELECT transaction_date, user_id, purchase_count
FROM recent_transactions
WHERE rank = 1
ORDER BY transaction_date;
