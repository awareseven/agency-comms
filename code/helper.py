# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# import data and rename columns 
# and convert date to dateobject
def import_data(filename):
    df = pd.read_csv(filename, dtype={
        "Likes": int,
        "Comments": int, 
        "Shares": int,
        "Länge": int
        }).rename(columns={
        'Veröffentlicht': 'date',
        'Post-URL': 'url',
        'Beitrag': 'text', 
        'Medienbeschreibung': 'media_description', 
        'Medientyp': 'media_type',
        'Medien-URL': 'media_url', 
        'Likes': 'likes', 
        'Comments': 'comments', 
        'Shares': 'shares',
        'Unnamed: 9': 'notavailable', 
        'Month': 'month', 
        'Länge': 'length',
        })
    df.date = pd.to_datetime(df["date"], dayfirst=True)
    df.text = df.text.fillna('')
    df["month_number"] = df.date.to_numpy('datetime64[M]').view('int64') % 12 + 1
    df["source"] = filename.replace(".csv", "")
    df["weekday"] = df.date.dt.day_name()
    df["month"] = df.date.dt.month_name()
    df["weeknumber"] = df.date.dt.isocalendar().week

    
    return df


def import_and_combine():
    df_BSI = import_data("BSI.csv")
    df_NCSC = import_data("NCSC.csv")
    df_CISA = import_data("CISA.csv")

    df = pd.concat([df_BSI, df_NCSC, df_CISA], ignore_index=True)
    df = df.drop(columns=["Monat", "notavailable"], axis = 1)
    return df

def basic_summary_stats(df):
    for source in df.source.unique():
        print(f"----------{source}----------")
        temp_df = df.loc[(df.source == source)]
        print(f"Number of posts: {len(temp_df)}")
        post_len_description = temp_df.length
        print(f"Mean of length: {post_len_description.mean()}")
        print(f"Median of length: {post_len_description.median()}")
        print(f"Standard deviation of length: {post_len_description.std()}")
        print(f"Min of length: {post_len_description.min()}")
        print(f"Max of length: {post_len_description.max()}")
        
        likes_description = temp_df.likes
        print("---likes---")
        print(f"Mean of likes: {likes_description.mean()}")
        print(f"Median of likes: {likes_description.median()}")
        print(f"Standard deviation of likes: {likes_description.std()}")
        print(f"Min of likes: {likes_description.min()}")
        print(f"Max of likes: {likes_description.max()}")
        
        comments_description = temp_df.comments
        print("---comments---")
        print(f"Mean of comments: {comments_description.mean()}")
        print(f"Median of comments: {comments_description.median()}")
        print(f"Standard deviation of comments: {comments_description.std()}")
        print(f"Min of comments: {comments_description.min()}")
        print(f"Max of comments: {comments_description.max()}")
        
        shares_description = temp_df.shares
        print("---shares---")
        print(f"Mean of shares: {shares_description.mean()}")
        print(f"Median of shares: {shares_description.median()}")
        print(f"Standard deviation of shares: {shares_description.std()}")
        print(f"Min of shares: {shares_description.min()}")
        print(f"Max of shares: {shares_description.max()}")
                
  
    
