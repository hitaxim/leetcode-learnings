SELECT 
    EXTRACT(month FROM activity_date) AS mon,
    activity_name,
    SUM(hours_spent)
FROM 
    user_activity
GROUP BY 
    EXTRACT(month FROM activity_date),
    activity_name
ORDER BY 
    mon,
    SUM(hours_spent) DESC;
