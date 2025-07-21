import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
from collections import Counter

import sqlite3

path="/Users/kristynaidzakovicova/Desktop/Data Analyst/git-commits/data-analyst-repo"
df=pd.read_csv(path+"/survey_data.csv")

# conn = sqlite3.connect('survey-data.sqlite')

# df.to_sql('main', conn, if_exists='replace', index=False)
# conn.close()

# checking data in the database
# conn = sqlite3.connect('survey-data.sqlite')

# QUERY = "SELECT * FROM main LIMIT 5"
# df_check = pd.read_sql_query(QUERY, conn)

# print(df_check)

# # count the number of rows in the table "main"
# QUERY = """
# SELECT COUNT(*) 
# FROM main
# """
# print(pd.read_sql_query(QUERY, conn))

# # display all tables in the database
# QUERY = """
# SELECT name as Table_Name FROM sqlite_master 
# WHERE type = 'table'
# """
# print(pd.read_sql_query(QUERY, conn))

# # group data by a specific column, like Age, to get the count of respondents in each age group
# QUERY = """
# SELECT Age, COUNT(*) as count
# FROM main
# GROUP BY Age
# ORDER BY Age
# """
# print(pd.read_sql_query(QUERY, conn))

# # get the schema of a specific table
# table_name = 'main'

# QUERY = """
# SELECT sql FROM sqlite_master 
# WHERE name= '{}'
# """.format(table_name)

# df_table = pd.read_sql_query(QUERY, conn)
# print(df_table.iat[0,0])

# T1: Plot a histogram of CompTotal (Total Compensation).
dist1 = df.dropna(subset="CompTotal").reset_index(drop=True)

Q1 = dist1["CompTotal"].quantile(0.25)
Q3 = dist1["CompTotal"].quantile(0.75)
IQR = Q3 - Q1
no_outliers = dist1[(dist1["CompTotal"] >= Q1 - 1.5*IQR) & (dist1["CompTotal"] <= Q3 + 1.5*IQR)]

plt.figure(figsize=(10,10))
sns.displot(data=no_outliers, x="CompTotal", stat='percent', kind='hist',bins=10)
plt.title("Distribution of CompTotal (after removing outliers)")
plt.xlabel("Total compensation")
plt.tight_layout()

plt.savefig(path+"/hist-CompTotal.png",format="png")

# T2: Plot a box plot of Age.
def replace_strings(row):
    if row == "35-44 years old":
        return (44+35)/2
    elif row =="18-24 years old":
        return (18+24)/2
    elif row =="45-54 years old":
        return (45+54)/2
    elif row =="55-64 years old":
        return (55+64)/2
    elif row =="65 years or older":
        return 65
    elif row =="Under 18 years old":
        return 18
    else:
        return np.nan

df["Age_clean"]=df["Age"].apply(replace_strings)
age1=df.dropna(subset="Age_clean").reset_index(drop=True)

plt.clf()
age1.plot(kind="box",column="Age_clean",title="Box plot of Age",xlabel="")
plt.tight_layout()
plt.savefig(path+"/box-age1.png",format="png")

# T3: Create a scatter plot of Age and WorkExp.
plt.clf()
df.plot(kind="scatter",x="Age_clean",y="WorkExp",xlabel="Age",ylabel="Work Experience",title="Scatter plot of Age and Work Experience")
plt.savefig(path+"/scatter-Age-WorkExp.png",format="png")

# T4: Create a bubble plot of TimeSearching and Frustration using the Age column as the bubble size.
# Frustration is not numeric, so can't do it

# T5: Create a pie chart of the top 5 databases(DatabaseWantToWorkWith) that respondents wish to learn next year.
def parse_databases(data):
    data_count = Counter()
    for row in data:
        if pd.isna(row):
            continue
        try:
            database = str(row).split(";")
            data_count.update(database)
        except (ValueError, AttributeError) as e:
            print(f"Error processing row: {row}. Error: {e}")
    return data_count

databases=parse_databases(df["DatabaseWantToWorkWith"])

combined_df = pd.DataFrame({
    'Databas': list(databases.keys()),
    'Count': list(databases.values())
}).sort_values("Count", ascending=False)

print(combined_df.head())

plt.clf()
combined_df.head().plot(kind="pie",y="Count",labels=combined_df["Databas"],title="Distribution of the top 5 databases users want to work with",xlabel="",ylabel="",legend=False,autopct='%1.1f%%')
plt.savefig(path+"/pie-databaseWantToWorkWith.png",format="png")

# T6: Create a stacked bar chart of median TimeSearching and TimeAnswering for the age group 30 to 35.
# Age data are not suitable for that.
# T7: Plot the median CompTotal for all ages from 45 to 60.
# Age data are not suitable for that.
# T8: Create a horizontal bar chart using the MainBranch column.
plt.clf()
branch=df["MainBranch"].value_counts()
branch.plot.barh(y="Count",title="Distribution of Main Branch",xlabel="Frequency",ylabel="")
# plt.tight_layout()
plt.savefig(path+"/barh-MainBranch.png",format="png")





