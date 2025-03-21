SELECT 
    u.UserID, 
    u.UserName, 
    COUNT(DISTINCT d.DeviceType) AS TotalDevices,
    SUM(s.StorageUsed) AS TotalStorageUsed
FROM 
    Users u
JOIN 
    Devices d ON u.UserID = d.UserID
JOIN 
    StorageUsage s ON d.DeviceID = s.DeviceID
GROUP BY 
    u.UserID, 
    u.UserName
HAVING 
    COUNT(DISTINCT d.DeviceType) > 1 AND SUM(s.StorageUsed) > 50
ORDER BY 
    TotalStorageUsed DESC;
