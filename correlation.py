import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

pwd="path/to/folder"

file_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv"
df = pd.read_csv(file_url)

# T1: Plot the distribution and histogram for ConvertedCompYearly to examine the spread of yearly compensation among respondents.
dist1 = df.dropna(subset="ConvertedCompYearly")
z = np.abs(stats.zscore(dist1["ConvertedCompYearly"]))
threshold = 3
no_outliers=dist1[z < threshold]
plt.figure(figsize=(10,6))

sns.displot(data=no_outliers, x="ConvertedCompYearly", stat='percent',kde=True, kind='hist')
plt.title("Distribution of ConvertedCompYearly without outliers")
plt.tight_layout()

plt.savefig(pwd+"/hist-ConvertedCompYearly.png",format="png")

# T2: Filter the data to calculate the median compensation for respondents whose employment status is "Employed, full-time."
fulltime=df[df["Employment"]=="Employed, full-time"]
median_comp=fulltime["ConvertedCompYearly"].median()
print(f"Median compensation for respondents with Employed, full-time is {median_comp}")

# T3: Create a new DataFrame by removing outliers from the ConvertedCompYearly column to get a refined dataset for correlation analysis.
# Previous task

# T4: Calculate correlations between ConvertedCompYearly, WorkExp, and JobSatPoints_1. Visualize these correlations with a heatmap.

corr=no_outliers[["ConvertedCompYearly","WorkExp","JobSatPoints_1"]].corr()
plt.clf()
sns.heatmap(corr)
plt.tight_layout()
plt.savefig(pwd+"/heatmap-corr.png",format="png")

# T5: Create scatter plots to examine specific correlations between ConvertedCompYearly and WorkExp, as well as between ConvertedCompYearly and JobSatPoints_1.

plt.clf()
fig, axs = plt.subplots(1,2,tight_layout=True,sharex=True,figsize=(20,6))
axs[0].scatter(x="ConvertedCompYearly",y="WorkExp",data=no_outliers,color="red",label="WorkExp")
axs[1].scatter(x="ConvertedCompYearly",y="JobSatPoints_1",data=no_outliers,color="blue",label="JobSatPoints")
for ax in axs:
    ax.legend(fancybox=False)
    ax.set_xlabel("ConvertedCompYearly")
plt.savefig(pwd+"/scatter-comp.png",format="png")