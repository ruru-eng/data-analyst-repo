import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

pwd="/Users/kristynaidzakovicova/Desktop/Data Analyst/git-commits/data-analyst-repo"

file_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv"
df = pd.read_csv(file_url)

# T1: Plot a bar chart to visualize the distribution of respondents by industry. Highlight any notable trends.
grp_industry=df.groupby(["Industry"]).size().reset_index(name="Count").sort_values("Count",ascending=True)

grp_industry.tail(10).plot(kind="barh",x="Industry",xlabel="Frequency",ylabel="",title="Distribution of respondents by industry (10 highest)",figsize=(10,6),legend=False)
plt.tight_layout()
plt.savefig(pwd+"/bar-Industry.png",format="png")

# T2: Identify respondents with extremely high yearly compensation.Calculate basic statistics (mean, median, and standard deviation) for ConvertedCompYearly. Identify compensation values exceeding a defined threshold (e.g., 3 standard deviations above the mean).
df.dropna(subset=["ConvertedCompYearly"],inplace=True)

mean_comp=df["ConvertedCompYearly"].mean()
med_comp=df["ConvertedCompYearly"].median()
print(med_comp)
std_comp=df["ConvertedCompYearly"].std()

high_comp=0
for row in df["ConvertedCompYearly"]:
    if row > (mean_comp+3*std_comp):
        high_comp+=1

print(f"The number of respondents with extremely high yearly compensation is {high_comp}.")

# T3: Identify outliers in the ConvertedCompYearly column using the IQR method. Calculate the Interquartile Range (IQR). Determine the upper and lower bounds for outliers. Count and visualize outliers using a box plot.

qr1=df["ConvertedCompYearly"].quantile(0.25)
qr3=df["ConvertedCompYearly"].quantile(0.75)

iqr=qr3-qr1

lowB=qr1-1.5*iqr
upB=qr3+1.5*iqr

plt.clf()
plt.boxplot(df["ConvertedCompYearly"])
plt.title("ConvertedCompYearly")
plt.savefig(pwd+"/boxplot-ConvertedCompYearly.png",format="png")

# T4: Remove outliers from the dataset. Create a new DataFrame excluding rows with outliers in ConvertedCompYearly. Validate the size of the new DataFrame.
z = np.abs(stats.zscore(df["ConvertedCompYearly"]))
threshold = 3
df_comp=df["ConvertedCompYearly"]

no_outliers=df_comp[z < threshold]
print(no_outliers.describe())

# T5: Analyze the correlation between Age (transformed) and other numerical columns. Map the Age column to approximate numeric values.Compute correlations between Age and other numeric variables. Visualize the correlation matrix.
# df[['bore','stroke','compression-ratio','horsepower']].corr()
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
df.dropna(subset="Age_clean",inplace=True)

corr_matrix=df.corr(numeric_only=True)
plt.clf()
sns.heatmap(corr_matrix)
plt.tight_layout()
plt.savefig(pwd+"/heatmap-Age.png",format="png")

# from scipy import stats
# df['stroke'].replace(np.nan,df['stroke'].astype('float').mean(axis=0),inplace=True)
# for column in df.columns.tolist():
#     if df.dtypes[column] == 'float64' or df.dtypes[column] == 'int64':
#         pearson_coef, p_value = stats.pearsonr(df[column], df['price'])
#         if p_value < 0.001:
#             print(f'{column} has c = {pearson_coef} and p-value = {p_value}')














