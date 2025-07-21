import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from collections import Counter

path="path/to/folder"
df=pd.read_csv(path+"/survey_data.csv")

# T2: Plot a histogram of YearsCodePro to analyze the distribution of coding experience among respondents.
def replace_strings(row):
    if row == "Less than 1 year":
        return 0
    elif row =="More than 50 years":
        return 50
    else:
        return row

df["YearsCodePro_clean"]=df["YearsCodePro"].apply(replace_strings)
df.dropna(subset="YearsCodePro_clean",inplace=True)
df["YearsCodePro_clean"]=df["YearsCodePro_clean"].astype("int")

sns.displot(data=df,x="YearsCodePro_clean",stat="percent", kind="hist",bins=10)
plt.title("Distribution of YearsCodePro")
plt.xlabel("YearsCodePro")
plt.tight_layout()

# T3: Use histograms to compare the distribution of CompTotal across different Age groups.
plt.clf()
dist1 = df.dropna(subset="CompTotal").reset_index(drop=True)

Q1 = dist1["CompTotal"].quantile(0.25)
Q3 = dist1["CompTotal"].quantile(0.75)
IQR = Q3 - Q1
no_outliers = dist1[(dist1["CompTotal"] >= Q1 - 1.5*IQR) & (dist1["CompTotal"] <= Q3 + 1.5*IQR)]

grouped = no_outliers.groupby(["Age"])

for name, group in grouped:
    plt.hist(group["CompTotal"].dropna(), alpha=0.5, bins=20, label=str(name))

plt.xlabel("Total Compensation")
plt.ylabel('Frequency')
plt.title('Distribution of CompTotal by Age Group')
plt.legend()

# T4: Use histograms to explore the distribution of TimeSearching (time spent searching for information) for respondents across different age groups.
plt.clf()
age2=df.groupby("Age").TimeSearching.value_counts().sort_index().unstack()
age2.plot.barh()
plt.xlabel("Frequency")
plt.title('Distribution of TimeSearching across different age groups')

# T5: Visualize the most desired databases for future learning using a histogram of the top 5 databases.
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

combined_df.index=combined_df["Databas"]

combined_df.head(5).plot.bar(legend=False)
plt.title("Distribution of the top 5 databases")
plt.xticks(rotation=0)
plt.xlabel("")
plt.ylabel("Frequency")

# T6: Use a histogram to explore the distribution of preferred work arrangements (remote work).
plt.clf()
df["RemoteWork"].value_counts().plot.bar()
plt.title("Distribution of preferred work arrangements")
plt.ylabel("Frequency")
plt.xticks(rotation=0)
plt.xlabel("")

# T7: Plot the histogram for JobSat scores based on respondents' years of professional coding experience.

grp_JobSat=df.groupby("JobSat").YearsCodePro.value_counts().unstack()
grp_JobSat.plot.barh()
plt.xlabel("Frequency")
plt.title('Distribution of JobSat across different profession coding experience')
