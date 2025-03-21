SELECT model_id, AVG(temperature) AS avg_temperature
FROM gpu_temps
GROUP BY model_id;
