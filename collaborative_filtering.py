# -*- coding: utf-8 -*-
"""collaborative_filtering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c8UkmfaGf7ij2Aq8-gCA_h-MUdwz3pEQ
"""

import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

ratings = pd.read_csv('toy_dataset.csv', index_col = 0)
ratings = ratings.fillna(0)

def standartize_row(row):
  row = (row - row.mean()) / (row.max() - row.min())
  return row

std_ratings = ratings.apply(standartize_row)
#To find similarity between items, items ought to be in rows.
item_sim = cosine_similarity(std_ratings.T)

item_sim_df = pd.DataFrame(item_sim, index = ratings.columns, columns = ratings.columns)
item_sim_df

def get_sim_movies(movie_name, user_rating):
  sim_score = item_sim_df[movie_name] * user_rating
  sim_score = sim_score.sort_values(ascending = False)
  return sim_score
print(get_sim_movies("action1", 5))

new_user = [("action1", 3), ("romantic1", 4), ("romantic2", 5)]
sim_movies = pd.DataFrame()

for movie_name, rating in new_user:
  sim_movies = sim_movies.append(get_sim_movies(movie_name, rating), ignore_index = True)
sim_movies.sum().sort_values(ascending = False)