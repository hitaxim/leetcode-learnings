import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('managerId').size().reset_index(name = 'manager')
    df = df.merge(employee[['id','name']], left_on = 'managerId', right_on = 'id', how = 'inner')
    result_df = df[df['manager'] >= 5]
    return result_df[['name']]

"""
SELECT E1.name FROM Employee E
JOIN Employee E1 ON E1.id = E.ManagerId
GROUP BY E1.id 
HAVING COUNT(E.ManagerId) >= 5;
"""
