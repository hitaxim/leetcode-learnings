SELECT w1.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate,w2.recordDate) = 1 AND w1.temperature > w2.temperature;


-----------------ORRRRRRR-----------


WITH q1 AS (
  SELECT 
      *,
      LAG(temperature) OVER (ORDER BY recordDate) AS previous_day_temperature,
      LAG(recordDate) OVER (ORDER BY recordDate) AS previous_Date
  FROM Weather
)

SELECT id
FROM q1
WHERE temperature > previous_day_temperature
AND DATEDIFF(recordDate, previous_Date) = 1;
