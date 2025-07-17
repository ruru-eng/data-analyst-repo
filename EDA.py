import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Load the Stack Overflow survey dataset
data_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv'
df = pd.read_csv(data_url)

# Display the first few rows of the dataset
# print(df.head())

pwd="path/to/folder"

# T1.1: Identify and manage missing values in critical columns such as Employment, JobSat, and RemoteWork. Implement a strategy to fill or drop these values, depending on the significance of the missing data.
cols=["Employment","JobSat","RemoteWork"]

df.dropna(subset=cols,inplace=True)
# T2.1: Create experience ranges for YearsCodePro (e.g., 0-5, 5-10, 10-20, >20 years).
df.dropna(subset="YearsCodePro",inplace=True)

def categorize_years(row):
    if row == "Less than 1 year":
        return "0-5 years"
    try:
        row = int(row)
    except (ValueError, TypeError):
        return None
    
    if row < 5:
        return "0-5 years"
    elif 5 <= row < 10:
        return "5-10 years"
    elif 10 <= row < 20:
        return "10-20 years"
    else:
        return ">20 years"

df["YearsCodePro_range"] = df["YearsCodePro"].apply(categorize_years)
    
# T2.2: Calculate the median JobSat for each range.
df_grp=df.groupby("YearsCodePro_range")["JobSat"].median().reset_index()

# T2.3: Visualize the relationship using a bar plot or similar visualization.
df_grp.plot(kind="bar",x="YearsCodePro_range",y="JobSat",title="Job satisfaction by Years coding",figsize=(10,6),legend=False,rot=0,xlabel="",ylabel="Job Satisfaction")
plt.savefig(pwd+"/bar-JobSat-YearsCodingPro.png",format="png")

# T3.1: Use a count plot to show the distribution of JobSat values. This provides insights into the overall satisfaction levels of respondents.
plt.clf()
sns.countplot(df,x="JobSat")
plt.savefig(pwd+"/countplot-JobSat.png",format="png")

# T4.1: Analyze trends in remote work based on job roles. Use the RemoteWork and Employment columns to explore preferences and examine if specific job roles prefer remote work more than others.

# T4.2: Use a count plot to show remote work distribution.
plt.clf()
sns.countplot(df,x="RemoteWork")
plt.title("Remote work distribution")
plt.xlabel("")
plt.savefig(pwd+"/countplot-RemoteWork.png",format="png")
# T4.3: Cross-tabulate remote work preferences by employment type (e.g., full-time, part-time) and job roles.
plt.clf()

def remove_noise(row):
    if re.search(r"\bfull-time\b",row):
        return "full-time"
    elif re.search(r"\bpart-time\b",row):
        return "part-time"

df["Fil_Employment"] = df["Employment"].apply(remove_noise)

df_pv=pd.crosstab(df["Fil_Employment"],df["RemoteWork"])
sns.heatmap(df_pv,cmap="coolwarm")
plt.title("Remote work preferences by employment type")
plt.xlabel("")
plt.ylabel("")
plt.tight_layout()
plt.savefig(pwd+"/heatmap-Employment-RemoteWork.png",format="png")

# T6.1: Examine how years of experience (YearsCodePro) correlate with job satisfaction (JobSatPoints_1). Use a scatter plot to visualize this relationship.
plt.clf()
grp_years=df.groupby("YearsCodePro_range")["JobSatPoints_1"].mean().reset_index()
grp_years.plot(kind='scatter',x="YearsCodePro_range",y="JobSatPoints_1",figsize=(5,5),rot=45,xlabel="",ylabel="Job Satisfaction Points")
plt.tight_layout()
plt.savefig(pwd+"/scatter-YearsCodePro-JobSatPoints_1.png",format="png")

# T7.1: Explore how educational background (EdLevel) relates to employment type (Employment). Use cross-tabulation and visualizations to understand if higher education correlates with specific employment types.
ed_empl_cross=pd.crosstab(df["Fil_Employment"],df["EdLevel"])
plt.clf()
plt.figure(figsize=(10,10))
sns.heatmap(ed_empl_cross,cmap="coolwarm",vmax=6000)
plt.title("Education background by Employment Type")
plt.xlabel("")
plt.ylabel("")
plt.tight_layout()
plt.savefig(pwd+"/heatmap-EdLevel_Employment.png",format="png")
# T8.1: After your analysis, save the modified dataset for further use or sharing.
df.to_csv(pwd+"/filtered-survey-data.csv")






