import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:

    merged = employees.merge(employee_uni, on='id', how='left')
    result = merged[['unique_id','name']]
    
    return result

"""
# Write your MySQL query statement below
select 
eu.unique_id as unique_id, e.name as name
from Employees e left join EmployeeUNI eu on e.id = eu.id
"""
