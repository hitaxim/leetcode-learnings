# Write your MySQL query statement below
SELECT DISTINCT e1.employee_id, e1.name, COUNT(e2.employee_id) AS reports_count,  ROUND(AVG(e2.age),0) AS average_age
FROM Employees e1, Employees e2
WHERE e2.reports_to IS NOT NULL AND e2.reports_to = e1.employee_id
GROUP BY e1.employee_id
ORDER BY e1.employee_id
