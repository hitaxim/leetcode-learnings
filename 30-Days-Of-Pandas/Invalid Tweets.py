import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid_tweet = tweets[tweets['content'].str.len() > 15]
    result = invalid_tweet[['tweet_id']]
    return result
    
