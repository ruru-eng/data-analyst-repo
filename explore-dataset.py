import pandas as pd

pd.set_option('display.max_rows', None)

df = pd.read_csv("../survey_data.csv")

# display the top 5 rows and columns of the dataset 
print(df.head())

# print the number of rows and columns in the dataset
print(df.shape)

# print datatype of each column
print(df.dtypes)

# print mean age of the survey participitants - use the most frequent one
print(df["Age"].value_counts())

# print how many unique countries are there in the Country column
print(len(df["Country"].unique()))
