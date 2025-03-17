SELECT MAX(salary) AS second_highest_salary
FROM employee
WHERE salary NOT IN 
(SELECT MAX(salary) FROM employee);
