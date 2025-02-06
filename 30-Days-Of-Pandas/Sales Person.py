import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    company = company.rename(columns = {'name': 'color'})

    df = orders.merge(company, on = 'com_id'
              ).merge(sales_person, on = 'sales_id')

    res = list(set(sales_person.name) - set(df[df.color == "RED"].name))
   
    return pd.DataFrame({'name':res})
