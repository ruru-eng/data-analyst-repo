import pandas as pd
import numpy as np

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv")

# T1.1: Count the number of duplicate rows in the dataset.
if len(df.duplicated().value_counts().index) == 1:
     print(f"The number of duplicate rows in the dataset is: 0")
else:
    print(f"The number of duplicate rows in the dataset is: {df.duplicated().value_counts().values[1]}")
# T1.2: Display the first few duplicate rows to understand their structure.
# There are no duplicates in the dataset.


# T2.1: Remove duplicate rows from the dataset using the drop_duplicates() function.
# There are no duplicates in the dataset.
# T2.2: Verify the removal by counting the number of duplicate rows after removal.
# There are no duplicates in the dataset.


# T3.1: Identify missing values for all columns in the dataset.
for col in df.columns:
    print(f"{col}")
    print(df[col].isna().value_counts())
# T3.2: Choose a column with significant missing values (e.g., EdLevel) and impute with the most frequent value.
print(f"Most frequent value in EdLevel column is {df['EdLevel'].value_counts().index[0]} with {df['EdLevel'].value_counts().values[0]} occurences.")


# T4.1: Use the ConvertedCompYearly column for compensation analysis as the normalized annual compensation is already provided.

# T4.2: Check for missing values in ConvertedCompYearly and handle them if necessary.
mean_comp=df["ConvertedCompYearly"].mean()
df_comp=df["ConvertedCompYearly"].replace(np.NaN,mean_comp)






