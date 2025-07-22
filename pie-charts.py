import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from collections import Counter

def del_outliers(data,col):   
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    return data[(data[col] >= Q1 - 1.5*IQR) & (data[col] <= Q3 + 1.5*IQR)]

def parser(data):
    count = Counter()
    for row in data:
        if pd.isna(row):
            continue
        try:
            dts = str(row).split(";")
            count.update(dts)
        except (ValueError, AttributeError) as e:
            print(f"Error processing row: {row}. Error: {e}")
    return count

path="/Users/kristynaidzakovicova/Desktop/Data Analyst/git-commits/data-analyst-repo"

df=pd.read_csv(path+"/survey_data.csv")

# T1: Create a Pie Chart of the Top 5 Databases Respondents Want to Work With
databases=parser(df["DatabaseWantToWorkWith"])

DatabaseWantToWorkWith = pd.DataFrame({
    'Databas': list(databases.keys()),
    'Count': list(databases.values())
}).sort_values("Count", ascending=False)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(DatabaseWantToWorkWith["Count"].head(), labels=DatabaseWantToWorkWith["Databas"].head(), autopct='%.1f%%')

plt.title("Distribution of top 5 databases respondents want to work with")
plt.xlabel("")
plt.ylabel("")
plt.tight_layout()


# T2: The DevType column lists the developer types for respondents. We’ll examine the distribution by showing the top 5 developer roles in a pie chart.

DevType=df["DevType"].value_counts().head()
fig, ax = plt.subplots(figsize=(12, 8))
ax.pie(DevType, labels=DevType.index, autopct='%.1f%%')

plt.title("Distribution of top 5 developer roles")
plt.xlabel("")
plt.ylabel("")
plt.tight_layout()


# T3: The OpSysProfessional use column shows the operating systems developers use professionally. Let’s visualize the distribution of the top operating systems in a pie chart.
OpSys=parser(df["OpSysProfessional use"])

OpSysProfessional = pd.DataFrame({
    "OpSys": list(OpSys.keys()),
    "Count": list(OpSys.values())
}).sort_values("Count", ascending=False)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(OpSysProfessional["Count"].head(), labels=OpSysProfessional["OpSys"].head(), autopct='%.1f%%')
plt.title("Distribution of top 5 operating systems respondents use professionally")
plt.xlabel("")
plt.ylabel("")
plt.tight_layout()
plt.show()
