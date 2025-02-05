SELECT IFNULL(U.unique_id, NULL) AS unique_id, name
FROM Employees E
LEFT JOIN EmployeeUNI U
ON E.id = U.id;
