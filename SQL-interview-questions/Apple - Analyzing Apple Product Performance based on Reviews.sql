SELECT EXTRACT(MONTH FROM submit_date) as mth, 
       product_id as product, 
       AVG(stars) as avg_stars
FROM reviews
GROUP BY mth, product
ORDER BY mth, product;
