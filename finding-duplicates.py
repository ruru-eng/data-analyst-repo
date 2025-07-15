import pandas as pd
import matplotlib.pyplot as plt

# load the dataset directly from the URL
pwd="path/to/file"
df = pd.read_csv(pwd+"/survey_data_with_duplicate.csv")

# display the first few rows
# print(df.head())

# T1.1: Count the number of duplicate rows in the dataset.
# print(df.duplicated().value_counts())
# T1.2: Display the first few duplicate rows to understand their structure.
df_duplicates=df[df.duplicated()]
print(df_duplicates.head())

# T2.1: Identify duplicate rows based on selected columns such as MainBranch, Employment, and RemoteWork. Analyse which columns frequently contain identical values within these duplicate rows.
# print(df.duplicated(subset=["MainBranch","RemoteWork","Employment"]).value_counts())
df_subset_duplicates=df[df.duplicated(subset=["MainBranch","RemoteWork","Employment"])]
print(df_subset_duplicates.head())


# T3.1: Create visualizations to show the distribution of duplicates across different categories.
distr=pd.DataFrame(df.duplicated().value_counts())
distr = distr.rename(columns={ 0: "count"})
distr.index = distr.index.map({True: 'Duplicated', False: 'Unique'})
print(distr)
distr.plot(kind="pie",y="count",legend=False)
plt.ylabel("")
plt.title(f"Distribution of duplicated values by all columns")
plt.savefig(pwd+"/duplicates-pie-all.png",format="png")
# T3.2: Use bar charts or pie charts to represent the distribution of duplicates by Country and Employment.
column="Employment"
if column in df.columns:
    distr=pd.DataFrame(df.duplicated(subset=column).value_counts())
    distr = distr.rename(columns={ 0: "count"})
    distr.index = distr.index.map({True: 'Duplicated', False: 'Unique'})
    print(distr)
    distr.plot(kind="pie",y="count",legend=False)
    plt.ylabel("")
    plt.title(f"Distribution of duplicated values by {column} column")
    plt.savefig(pwd+"/duplicates-pie.png",format="png")


# T4.1: Decide which columns are critical for defining uniqueness in the dataset.
df_unique=df.drop_duplicates(keep="last",ignore_index=True)
print(df_unique.head())
# T4.2: Remove duplicates based on a subset of columns if complete row duplication is not a good criterion.

# T5.1:Document the process of identifying and removing duplicates. 
# The only good solution is to remove only full row duplicates as it represents duplicate entries. 



