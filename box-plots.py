import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sqlite3

def del_outliers(data,col):   
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    return data[(data[col] >= Q1 - 1.5*IQR) & (data[col] <= Q3 + 1.5*IQR)]

conn = sqlite3.connect('survey-results-public.sqlite')

# T1: Box Plot of CompTotal
QUERY = "SELECT CompTotal FROM main"
CompTotal = pd.read_sql_query(QUERY, conn)

CompTotal.dropna(inplace=True)

CompTotal.plot.box(title="Box plot of Total compensation (unfiltered)",xlabel="")

# T2: Convert the Age column into numerical values and visualize the distribution.
QUERY = "SELECT Age FROM main"
Age = pd.read_sql_query(QUERY, conn)

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

Age["Age_clean"]=Age["Age"].apply(replace_strings)
age1=Age.dropna(subset="Age_clean").reset_index(drop=True)

age1.plot.box(title="Box plot of Age",xlabel="")

# T3: Box Plot of CompTotal Grouped by Age Groups
QUERY = "SELECT CompTotal, Age FROM main"
GRP_CompTotal = pd.read_sql_query(QUERY, conn)
GRP_CompTotal.dropna(inplace=True)

no_out = del_outliers(GRP_CompTotal,"CompTotal")

plt.figure(figsize=(14, 8))
ax=sns.boxplot(x="Age", y="CompTotal", data=no_out)
plt.tight_layout()

# T4: Box Plot of CompTotal Grouped by Job Satisfaction (JobSatPoints_6):
QUERY = "SELECT CompTotal, JobSatPoints_6 FROM main"
GRP_JobSatPoints_6 = pd.read_sql_query(QUERY, conn)
GRP_JobSatPoints_6.dropna(inplace=True)

no_out = del_outliers(GRP_JobSatPoints_6,"CompTotal")

plt.figure(figsize=(14, 8))
ax=sns.boxplot(x="JobSatPoints_6", y="CompTotal", data=no_out)
ax.set_xticklabels(no_out["JobSatPoints_6"].unique(), rotation=45, ha='right', fontsize=9)
plt.tight_layout()

# T5: Box Plot of ConvertedCompYearly for the Top 5 Developer Types
QUERY = "SELECT * FROM main"
full_df = pd.read_sql_query(QUERY, conn)

no_out = del_outliers(full_df,"CompTotal")

plt.figure(figsize=(14, 8))
ax=sns.boxplot(x="MainBranch", y="CompTotal", data=no_out)
plt.tight_layout()

# T6: Box Plot of CompTotal for the Top 5 Countries
plt.figure(figsize=(14, 8))
country_data=no_out["Country"].value_counts().head()
countries=no_out[no_out["Country"].isin(country_data.index)]

ax=sns.boxplot(x="Country", y="CompTotal", data=countries)
plt.tight_layout()
plt.show()

conn.close()
