SELECT r.region_name, SUM(h.unit_cost * p.quantity) AS total_cost
FROM hardware h
JOIN production p ON h.hardware_id = p.hardware_id
JOIN region r ON p.production_id = r.production_id
WHERE MONTH(p.production_date) = 6 AND YEAR(p.production_date) = 2022
GROUP BY r.region_name;
