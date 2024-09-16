WITH CTE AS (
   SELECT num,
   LAG(num,1) OVER() num1,
   LEAD(num,1) OVER()  num2
   FROM Logs
)


SELECT DISTINCT num AS ConsecutiveNums
FROM CTE
WHERE num1 = num AND num = num2
