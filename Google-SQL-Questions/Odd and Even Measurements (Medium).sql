
WITH RankedMeasurements AS (
    SELECT 
        DATE(measurement_time) AS measurement_day,
        measurement_value,
        ROW_NUMBER() OVER (PARTITION BY DATE(measurement_time) ORDER BY measurement_time) AS measurement_order
    FROM measurements
)
SELECT 
    measurement_day,
    SUM(CASE WHEN measurement_order % 2 = 1 THEN measurement_value ELSE 0 END) AS odd_sum,
    SUM(CASE WHEN measurement_order % 2 = 0 THEN measurement_value ELSE 0 END) AS even_sum
FROM RankedMeasurements
GROUP BY measurement_day
ORDER BY measurement_day;


/*
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
*/
