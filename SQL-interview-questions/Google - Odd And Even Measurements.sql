WITH ranked_measurement AS (
  SELECT CAST(measurement_time AS DATE) AS measurement_day, 
  measurement_value, 
  ROW_NUMBER() OVER (
  PARTITION BY CAST(measurement_time AS DATE)
  ORDER BY measurement_time) AS measurement_num
  FROM measurements
)

SELECT measurement_day, 
SUM(measurement_value) FILTER (WHERE measurement_num % 2 != 0) AS odd_sum, 
SUM(measurement_value) FILTER (WHERE measurement_num % 2 = 0) AS even_sum
FROM ranked_measurement
GROUP BY measurement_day;
