import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv"
df = pd.read_csv(file_path)

# T1: Identify duplicate rows in the dataset.
for i,ind in enumerate(df.duplicated().value_counts().index):
    if ind == True:
        print(f"The number of duplicated rows in the dataset is {df.duplicated().value_counts().values[i]}.")
    else:
        print(f"There are no duplicated rows in the dataset.")

# T2: Remove the duplicate rows from the dataframe.
# There are no duplicated rows in the dataset. 
# T3: Find the missing values for all columns.
for col in df.columns:
    print(col)
    for i,ind in enumerate(df[col].isnull().value_counts().index):
        if ind == True:
            print(f"The number of missing rows: {df[col].isnull().value_counts().values[i]}.")
        elif df[col].isnull().value_counts().values[i] == df.shape[0]:
            print(f"There are no missing rows in column.")

# T4: Find out how many rows are missing in the column RemoteWork.
col="RemoteWork"
for i,ind in enumerate(df[col].isnull().value_counts().index):
        if ind == True:
            print(f"The number of missing rows in {col}: {df[col].isnull().value_counts().values[i]}.")
        elif df[col].isnull().value_counts().values[i] == df.shape[0]:
            print(f"There are no missing rows in column.")

# T5: Find the value counts for the column RemoteWork.
print(f"The number of rows in column {col} is {df[col].shape[0]}.")

# T6: Identify the most frequent (majority) value in the RemoteWork column.
most_freq=df[col].value_counts().index[0]
print(f"The most frequent value in column {col} is {most_freq}.")

# T7: Impute (replace) all the empty rows in the column RemoteWork with the majority value.
print(df[col].isna().value_counts())
df[col].replace(np.nan,most_freq,inplace=True)
print(df[col].isna().value_counts())
