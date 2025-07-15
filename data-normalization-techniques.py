import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv")

pwd="path/to/work/folder"
# Replace NaN values with mean value.
# mean_value=df["ConvertedCompYearly"].mean()
# df["ConvertedCompYearly"].replace(np.nan,mean_value,inplace=True)

df["ConvertedCompYearly"].dropna(inplace=True)

# Task 5: Normalize ConvertedCompYearly using Min-Max Scaling.
df["ConvertedCompYearly_min_max"]=(df["ConvertedCompYearly"]-df["ConvertedCompYearly"].min())/(df["ConvertedCompYearly"].max()-df["ConvertedCompYearly"].min())
print(df["ConvertedCompYearly_min_max"].describe())

# Task 6: Apply Z-score Normalization to ConvertedCompYearly.
df["ConvertedCompYearly_Zscore"]=(df["ConvertedCompYearly"]-df["ConvertedCompYearly"].mean())/df["ConvertedCompYearly"].std()
print(df["ConvertedCompYearly_Zscore"].describe())
# Task 7: Visualize the distribution of ConvertedCompYearly, ConvertedCompYearly_Normalized, and ConvertedCompYearly_Zscore
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

ax1.hist(df["ConvertedCompYearly"], bins='auto')
ax1.set_title("Original Data")

ax2.hist(df["ConvertedCompYearly_min_max"], bins='auto')
ax2.set_title("Min-Max Scaled")

ax3.hist(df["ConvertedCompYearly_Zscore"], bins='auto')
ax3.set_title("Z-Score Normalized")

plt.tight_layout()

plt.savefig(pwd+"/dist-comp.png",format="png")

