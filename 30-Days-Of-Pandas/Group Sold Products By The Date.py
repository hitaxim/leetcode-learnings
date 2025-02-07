import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    
    df = activities.groupby('sell_date').agg(
        num_sold = ('product','nunique'),
        products = ('product',  lambda x: ','.join(sorted(set(x))))  # Sort and join unique product names
    ).reset_index()
    
    return df

"""
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    grouped = activities.groupby('sell_date')['product'].agg(['nunique', lambda x: ','.join(sorted(set(x)))]).reset_index()
    
    
    grouped.columns = ['sell_date', 'num_sold', 'products']
    
   
    grouped['products'] = grouped['products'].str.replace(r'(^|,)Mask(,|$)', r'\1Mask\2')
    
    # Sort the result table by sell_date
    result = grouped.sort_values(by='sell_date')
    
    return result
"""
