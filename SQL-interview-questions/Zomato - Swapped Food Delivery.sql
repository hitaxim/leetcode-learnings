WITH order_counts AS (
  SELECT COUNT(order_id) AS total_orders 
  FROM orders
)

SELECT 
  CASE 
    WHEN order_id % 2 != 0 AND order_id != total_orders THEN order_id + 1
    WHEN order_id % 2 != 0 AND order_id = total_orders THEN order_id
    ELSE order_id - 1
  END AS corrected_order_id,
  item
FROM orders
CROSS JOIN order_counts
ORDER BY corrected_order_id;

/*** ORRRRR */
WITH swapped_orders AS (
    SELECT 
        CASE 
            WHEN MOD(order_id, 2) = 1 AND LEAD(order_id) OVER (ORDER BY order_id) IS NOT NULL 
            THEN LEAD(item) OVER (ORDER BY order_id)
            WHEN MOD(order_id, 2) = 0 
            THEN LAG(item) OVER (ORDER BY order_id)
            ELSE item
        END AS corrected_item,
        order_id
    FROM orders
)
SELECT order_id, corrected_item AS item
FROM swapped_orders
ORDER BY order_id;
