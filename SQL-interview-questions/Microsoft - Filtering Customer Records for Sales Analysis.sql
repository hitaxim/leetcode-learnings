SELECT *
FROM Sales
WHERE product_type = 'Software'
AND sales_year > 2015
AND NOT sales_region = 'Europe'
