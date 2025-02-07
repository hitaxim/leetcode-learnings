import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [
            accounts[accounts.income < 20000].shape[0],
            accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].shape[0],
            accounts[accounts.income > 50000].shape[0],
        ],
    })

"""
# Write your MySQL query statement below
SELECT 'Low Salary' AS category, 
       COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 20000

UNION ALL

SELECT 'Average Salary' AS category, 
       COUNT(*) AS accounts_count
FROM Accounts
WHERE income BETWEEN 20000 AND 50000

UNION ALL

SELECT 'High Salary' AS category, 
       COUNT(*) AS accounts_count
FROM Accounts
WHERE income > 50000;
"""
