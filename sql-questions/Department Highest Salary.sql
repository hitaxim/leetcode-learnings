SELECT
   Department.name AS Department,
   Employee.name AS Employee,
   Salary
FROM
   Employee
JOIN
   Department
   ON Department.id = Employee.departmentId
WHERE
   (Employee.departmentId, Salary) IN (
       SELECT
           departmentId,
           MAX(Salary)
       FROM
           Employee
       GROUP BY
           departmentId
   );
