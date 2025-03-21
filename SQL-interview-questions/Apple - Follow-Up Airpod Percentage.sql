
WITH lag_products AS (
  SELECT
  customer_id,
  product_name,
  LAG(product_name)
    OVER(PARTITION BY customer_id
    ORDER BY transaction_timestamp) AS prev_prod
  FROM transactions
  GROUP BY
  customer_id,
  product_name,
  transaction_timestamp
),
interested_users AS (
  SELECT customer_id AS airpod_iphone_buyers
  FROM lag_products
  WHERE LOWER(product_name) = 'airpods'
    AND LOWER(prev_prod) = 'iphone'
  GROUP BY customer_id
)

SELECT
ROUND(
  COUNT(DISTINCT iu.airpod_iphone_buyers)::DECIMAL
  / COUNT(DISTINCT transactions.customer_id)::DECIMAL
  * 100, 0)
FROM transactions
LEFT JOIN interested_users AS iu
  ON iu.airpod_iphone_buyers = transactions.customer_id;
