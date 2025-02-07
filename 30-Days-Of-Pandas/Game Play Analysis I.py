import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login_df = activity.groupby('player_id')['event_date'].agg(min).reset_index()

    first_login_df = first_login_df.rename(columns={'event_date': 'first_login'})

    return first_login_df

"""
select player_id,min(event_date) as first_login
from Activity
group by player_id
"""
