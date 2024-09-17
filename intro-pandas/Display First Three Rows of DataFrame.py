import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
   x = employees.head(3)
   return x
