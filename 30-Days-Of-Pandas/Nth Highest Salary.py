import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if employee.empty or 'salary' not in employee.columns or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Drop duplicate salaries and sort in descending order
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # Check if there are enough salaries for the nth highest
    if N > len(unique_salaries):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Fetch the nth highest salary
    nth_salary = unique_salaries.iloc[N-1]
    
    # Return as a DataFrame with dynamic column name
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})
