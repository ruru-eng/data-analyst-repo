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

# T1: Visualize the relationship between respondents' age (Age) and job satisfaction (JobSatPoints_6). Use this plot to identify any patterns or trends.
fig, ax = plt.subplots(figsize=(12, 8))
sns.stripplot(
    data=df,
    x="Age",
    y="JobSatPoints_6",
    ax=ax,
    jitter=True 
)
plt.title("Scatter plot of respondents' Age and Job Satisfaction")
plt.xlabel("")
plt.tight_layout()

# T2: Explore the relationship between yearly compensation (ConvertedCompYearly) and job satisfaction (JobSatPoints_6) using a scatter plot.
plt.cla()
clear_CompYearly=del_outliers(df,"ConvertedCompYearly")

sns.scatterplot(
    data=clear_CompYearly,
    x="ConvertedCompYearly",
    y="JobSatPoints_6",
    ax=ax
)
plt.title("Scatter plot of respondents' Yearly compensation and Job Satisfaction (prefiltered)")
plt.xlabel("Yearly compensation")
plt.tight_layout()

# T3: Create a bubble plot to explore the relationship between yearly compensation (ConvertedCompYearly) and job satisfaction (JobSatPoints_6), with bubble size representing age.
plt.cla()
sns.scatterplot(
    data=clear_CompYearly,
    x="ConvertedCompYearly",
    y="JobSatPoints_6",
    ax=ax,
    size="Age",
    hue="Age"
)
plt.title("Scatter plot of respondents' Yearly compensation and Job Satisfaction (prefiltered, colored by Age)")
plt.xlabel("Yearly compensation")
plt.tight_layout()
