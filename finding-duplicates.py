import pandas as pd
import matplotlib.pyplot as plt

# load the dataset directly from the URL
file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VYPrOu0Vs3I0hKLLjiPGrA/survey-data-with-duplicate.csv"
df = pd.read_csv(file_path)

# display the first few rows
# print(df.head())

# T1.1: Count the number of duplicate rows in the dataset.
print(df[df.duplicated()])
# T1.2: Display the first few duplicate rows to understand their structure.
