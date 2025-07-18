# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from scipy import stats

# ---------------------------------------------------------------------------------
pwd="path/to/folder"
# ---------------------------------------------------------------------------------

data_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv'
df = pd.read_csv(data_url)
df=df.head(100)

#T1 Display the column names, data types, and summary information to understand the data structure.
# print(df.columns.values)
# print(df.dtypes)
# print(df.describe(include="all"))

# T2: Identify missing values in the dataset. Impute or remove missing values as necessary to ensure data completeness. NOTE: removing values only in columns I need
# for col in df.columns:
#     print(col)
#     print(df[col].isna().value_counts())

# T3: Calculate the value counts for Employment, JobSat and YearsCodePro columns to understand the distribution of responses.
# cols=["Employment","JobSat","YearsCodePro"]
# for col in cols:
#     print(df[col].value_counts())

# T4: Create a pie chart or KDE plot to visualize the distribution of JobSat.
plt.figure(figsize=(10,6))
sns.kdeplot(df,x="JobSat")
plt.title("Distribution of Job Satisfaction")
plt.xlabel("Job Satisfaction")
plt.ylabel("Density")
plt.xlim(0,11)
plt.xticks([1,2,3,4,5,6,7,8,9,10])
plt.tight_layout()
plt.savefig(pwd+"/kde-JobSat.png",format="png")

# T5: Compare the frequency of programming languages in LanguageHaveWorkedWith and LanguageWantToWorkWith. Visualize the overlap or differences using a Venn diagram or a grouped bar chart.


def parse_lang(data):
    lang_count = Counter()
    for row in data:
        if pd.isna(row):
            continue
        try:
            languages = str(row).split(";")
            lang_count.update(languages)
        except (ValueError, AttributeError) as e:
            print(f"Error processing row: {row}. Error: {e}")
    return lang_count

lang_want=parse_lang(df["LanguageWantToWorkWith"])
lang_have=parse_lang(df["LanguageHaveWorkedWith"])

combined_df = pd.DataFrame({
    'Language': list(lang_have.keys()),
    'HaveWorkedWith': list(lang_have.values()),
    'WantToWorkWith': [lang_want.get(lang, 0) for lang in lang_have.keys()]
}).sort_values('HaveWorkedWith', ascending=False)

fil_comb=combined_df.iloc[0:11]

plt.clf()
plt.figure(figsize=(10,6))

fil_comb.plot(kind="barh",x="Language",y=["HaveWorkedWith","WantToWorkWith"],ylabel="")
plt.tight_layout()
plt.savefig(pwd+"/bar-Languages.png",format="png")

# T6: Visualize the distribution of RemoteWork by region using a grouped bar chart or heatmap.

grp_remote = df.groupby(["Country", "RemoteWork"]).size().reset_index(name="Count")
remote_pivot = grp_remote.pivot(index="Country", columns="RemoteWork", values="Count").fillna(0)


plt.clf()
plt.figure(figsize=(20,12))
remote_pivot.plot(kind="barh",xlabel="Frequency",ylabel="")
plt.legend(loc="lower left",bbox_to_anchor=(-0.5, 1),fancybox=False)
plt.tight_layout()
plt.savefig(pwd+"/bar-RemoteWork.png",format="png")

# T7: Analyze the correlation between overall job satisfaction (JobSat) and YearsCodePro. Calculate the Pearson or Spearman correlation coefficient.

def replace_strings(row):
    if row == "Less than 1 year":
        return 0.5
    elif row =="More than 50 years":
        return 50
    else:
        return row

df["YearsCodePro_clean"]=df["YearsCodePro"].apply(replace_strings)
df.dropna(subset=["YearsCodePro_clean","JobSat"],inplace=True)

pear, p_value = stats.pearsonr(df["JobSat"].astype("float"),df["YearsCodePro_clean"].astype("float"))
print(f"c = {pear} and p-value = {p_value}")

# T8: Analyze the relationship between employment status (Employment) and education level (EdLevel). Create a cross-tabulation using pd.crosstab() and visualize it with a stacked bar plot if possible.
crs_empl_ed=pd.crosstab(df["Employment"],df["EdLevel"])
plt.clf()
plt.figure(figsize=(20,12))
crs_empl_ed.plot(kind="barh",xlabel="Frequency",ylabel="")
plt.legend(loc="best",fancybox=False,fontsize=6)
plt.tight_layout()
plt.savefig(pwd+"/bar-Employment-EdWork.png",format="png")

# T9: Save the cleaned dataset to a new CSV file for further use or sharing.
df.to_csv(pwd+"/filtered-survey-data-2.csv")





