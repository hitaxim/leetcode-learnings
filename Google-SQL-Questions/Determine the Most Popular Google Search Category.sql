SELECT 
  categories.category_name, 
  EXTRACT(MONTH FROM searches.search_date) AS month, 
  COUNT(*) OVER (PARTITION BY categories.category_name, EXTRACT(MONTH FROM searches.search_date)) AS total_searches
FROM
  searches
LEFT JOIN 
  categories ON categories.category_id = searches.category_id
WHERE
  EXTRACT(YEAR FROM searches.search_date) = 2024
ORDER BY
  total_searches DESC
