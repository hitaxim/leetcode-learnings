import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    
    # Drop id column & Sort the DataFrame by score in descending order
    result_df = scores.drop('id',axis=1).sort_values(by='score', ascending=False)
    
    return result_df

"""
SELECT s.Score, count(distinct t.score) Rank
FROM Scores s JOIN Scores t ON s.Score <= t.score
GROUP BY s.Id
ORDER BY s.Score desc
"""
