import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv"

pwd="path/to/work-folder"
df=pd.read_csv(file_path)

# T1: Display basic information and summary statistics of the dataset.
print(df.describe(include="all"))

# T2: Identify missing values for all columns.
for col in df.columns:
    print(df[col].isnull())

# T3: Visualize missing values using a heatmap (Using seaborn library).
plt.figure(figsize=(20,20))
sns.heatmap(df.isnull(),cmap="coolwarm")
plt.savefig(pwd+"/null-heatmap.png",format="png")

# T4: Count the number of missing rows for a specific column (e.g., Employment).
col="Employment"
for i,ind in enumerate(df[col].isnull().value_counts().index):
    if ind == True:
        print(f"The number of missing rows in column {col} is {df[col].isnull().value_counts().values[i]}.")
    else:
        print(f"There are no missing rows in column {col}.")

# T5: Identify the most frequent (majority) value in a specific column (e.g., Employment).
print(f"Most frequent value in {col} column is {df[col].value_counts().index[0]} with {df[col].value_counts().values[0]} occurences.")

# T6: Impute missing values in the specific column (e.g., Employment) with the most frequent value.
most_freq=df[col].value_counts().values[0]
df[col].replace(np.nan,most_freq,inplace=True)

# T7: Visualize the distribution of a column after imputation (e.g., Employment).
if col in df.columns:
    distr=pd.DataFrame(df[col].value_counts())
    distr.plot(kind="pie",y=col,legend=False,autopct='%1.1f%%')
    plt.ylabel("")
    plt.title(f"Distribution of values in {col} column")
    plt.savefig(pwd+f"/distr-{col}.png",format="png")
