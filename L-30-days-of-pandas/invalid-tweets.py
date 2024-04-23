'''
Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.
Return the result table in any order.
The result format is in the following example.
'''
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid_tweets = tweets[tweets['content'].str.len()>15]
    invalid_tweets = invalid_tweets[['tweet_id']]
    return invalid_tweets
