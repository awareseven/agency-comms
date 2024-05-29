# -*- coding: utf-8 -*-
"""
Analysis of LinkedIn posts of national 
 cyber security agencies
- BSI (DE)
- NCSC (UK)
- CISA (USA)
"""
import numpy as np
import pandas as pd
import helper
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords


df = helper.import_and_combine()
#uncomment to only analyse specific month, i.e. march 
#df = df[df.month == "March"]

helper.basic_summary_stats(df)

plt.figure(figsize=(10,2))
sns.boxplot(data=df, x="length", y="source", hue="source")
plt.xlabel("Length of Posts")
plt.ylabel("Agency")
plt.tight_layout()
plt.plot()
plt.savefig("images/post_length.png")

plt.figure(figsize=(10,2))
sns.boxplot(data=df, x="likes", y="source", hue="source")
plt.xlabel("Number of Likes")
plt.ylabel("Agency")
plt.tight_layout()
plt.plot()
plt.savefig("images/likes.png")

plt.figure(figsize=(10,2))
sns.boxplot(data=df, x="comments", y="source", hue="source")
plt.xlabel("Number of Comments")
plt.ylabel("Agency")
plt.tight_layout()
plt.plot()
plt.savefig("images/comments.png")

plt.figure(figsize=(10,2))
sns.boxplot(data=df, x="shares", y="source", hue="source")
plt.xlabel("Number of Shares")
plt.ylabel("Agency")
plt.tight_layout()
plt.plot()
plt.savefig("images/shares.png")


for agency in ["BSI", "CISA", "NCSC"]:
    plt.figure(figsize=(10,5))
    sns.stripplot(data=df[df.source == agency].sort_values(by=['month_number']), y="length", x="month", hue="month", legend=False)
    plt.title(f"{agency}")
    plt.tight_layout()
    plt.plot() 
    plt.savefig(f"images/{agency}_month_length.png")

for agency in ["BSI", "CISA", "NCSC"]:
    plt.figure(figsize=(10,5))
    sns.stripplot(data=df[df.source == agency].sort_values(by=['month_number']), y="likes", x="month", hue="month", legend=False)
    plt.title(f"{agency}")
    plt.tight_layout()
    plt.plot()
    plt.savefig(f"images/{agency}_month_likes.png")

for agency in ["BSI", "CISA", "NCSC"]:
    plt.figure(figsize=(10,5))
    sns.stripplot(data=df[df.source == agency].sort_values(by=['month_number']), y="comments", x="month", hue="month", legend=False)
    plt.title(f"{agency}")
    plt.tight_layout()
    plt.plot()
    plt.savefig(f"images/{agency}_month_comments.png")

for agency in ["BSI", "CISA", "NCSC"]:
    plt.figure(figsize=(10,5))
    sns.stripplot(data=df[df.source == agency].sort_values(by=['month_number']), y="shares", x="month", hue="month", legend=False)
    plt.title(f"{agency}")
    plt.tight_layout()
    plt.plot()
    plt.savefig(f"images/{agency}_month_shares.png")

for agency in ["BSI", "CISA", "NCSC"]:
    plt.figure(figsize=(10,5))
    sns.scatterplot(data=df[df.source == agency], y="likes", x="length", legend=False)
    plt.title(f"{agency}")
    plt.tight_layout()
    plt.plot()
    plt.savefig(f"images/{agency}_length_likes.png")

for agency in ["BSI", "CISA", "NCSC"]:
    plt.figure(figsize=(10,5))
    sns.stripplot(data=df[df.source == agency], y="length", x="weekday", legend=False)
    plt.title(f"{agency}")
    plt.tight_layout()
    plt.gca().invert_xaxis()
    plt.plot()
    plt.savefig(f"images/{agency}_weekday_length.png")
    
for agency in ["BSI", "CISA", "NCSC"]:
    plt.figure(figsize=(10,5))
    sns.stripplot(data=df[df.source == agency], y="likes", x="weekday", legend=False)
    plt.title(f"{agency}")
    plt.tight_layout()
    plt.gca().invert_xaxis()
    plt.plot()
    plt.savefig(f"images/{agency}_weekday_likes.png")



plt.figure(figsize=(3,5), dpi=200)
sns.histplot(data=df, hue="media_type", x="source", multiple="fill")
plt.title("Media Types")
plt.tight_layout()
#plt.legend(title = "Media Types", labels=["Video", "Image", "No Media", "Document"])
plt.plot()
plt.savefig("images/media_types.png")


# media type vs likes etc? 
for typ in ["likes", "shares", "comments"]:
    plt.figure()#figsize=(3,5))
    sns.boxplot(df, hue="media_type", x=typ, y="source", vert=False)
   # plt.tight_layout()
    plt.plot()
    plt.savefig(f"images/media_types_{typ}.png")
    

    
# length vs likes all in one 
plt.figure(figsize=(10,5))
sns.scatterplot(data=df, y="likes", x="length", hue = "source", legend=True, alpha=0.3)
plt.title(f"All Agencies")
plt.tight_layout()
plt.plot()
plt.savefig(f"images/all_in_one_length_likes.png")

