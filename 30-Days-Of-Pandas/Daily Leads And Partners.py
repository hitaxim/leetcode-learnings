import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    grouped = daily_sales.groupby(['date_id', 'make_name']).agg({'lead_id': 'nunique', 'partner_id': 'nunique'}).reset_index()
    
    grouped.columns = ['date_id', 'make_name', 'unique_leads', 'unique_partners']
    
    return grouped
    
