import pandas as pd

df1 = pd.read_csv("Merged_TMDB_tvShow_URLs.csv")
df2 = pd.read_csv("tmdb_movies_URLs.csv")

merged_data = pd.concat([df1,df2], ignore_index=True)
merged_df = merged_data.drop_duplicates(subset=["Url"])

merged_df.to_csv("TMDB_URLs.csv", index=False)
