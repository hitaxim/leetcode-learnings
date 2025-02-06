import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views['id'] = views.loc[views['author_id'] == views['viewer_id'],['viewer_id']]
    views['id'] = views['id'].drop_duplicates()
    views.dropna(inplace=True)
    views.sort_values(by='id', inplace=True)
    return views[['id']]
    
