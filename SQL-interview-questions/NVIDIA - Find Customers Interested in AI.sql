SELECT
  customer_id,
  name,
  email
FROM
  Customers
WHERE
  interests LIKE '%AI%';
