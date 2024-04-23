'''
Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The result format is in the following example.
'''
import pandas as pd

def article_views(df: pd.DataFrame) -> pd.DataFrame:
    #check is there same value in column 'author_id' and 'viewer_id'
    #drop the duplicate
    #sort by ascending
    df = df[df['author_id'] == df['viewer_id']][['author_id']]
    df = df.drop_duplicates().sort_values(by=['author_id'])
    #rename the column to id
    df.columns = ['id']
    #return the df
    return df
