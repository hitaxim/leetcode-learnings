WITH total_tweets AS (
  SELECT user_id, 
  COUNT(tweet_id) AS tweet_count_per_user
  FROM tweets
  WHERE tweet_date BETWEEN '2022-01-01' AND '2022-12-31'
  GROUP BY user_id
)

SELECT tweet_count_per_user AS tweet_bucket,
  COUNT(user_id) AS users_num
  FROM total_tweets
  GROUP BY tweet_count_per_user;

"""
  WITH CTE AS (
  SELECT COUNT(tweet_id) AS tweet_counts, user_id
  FROM tweets
  WHERE EXTRACT(year FROM tweet_date) = 2022
  GROUP BY user_id
)

SELECT tweet_counts AS tweet_bucket, 
COUNT(user_id) AS users_num
FROM CTE
GROUP BY tweet_counts;
  """
