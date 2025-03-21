SELECT
  DISTINCT product.product_line,
  SUM(amount) OVER (
    PARTITION BY product.product_line) AS total_revenue
FROM transactions
INNER JOIN product_info AS product
  ON transactions.product_id = product.product_id
ORDER BY total_revenue DESC;
