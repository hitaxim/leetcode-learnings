WITH cte AS (
SELECT 
  category, product, 
  SUM(spend) AS spent_t, 
  RANK() OVER (PARTITION BY category ORDER BY SUM(spend) DESC) AS ranks
  FROM product_spend
  WHERE EXTRACT(YEAR FROM transaction_date) = 2022
  GROUP BY category, product
)

SELECT category, product,
  spent_t AS total_spend
  FROM cte 
  WHERE ranks <= 2
  ORDER BY category, ranks;
