# Grouping:

# importing the necessary libraries
import pandas as pd

# loading the dataset
data = pd.read_csv('data.csv')

# group by a categorical variable and calculate the mean of a numerical variable
grouped_data = data.groupby('category')['numerical_variable'].mean()

# group by multiple variables and calculate the sum of another variable
grouped_data2 = data.groupby(['category', 'sub_category'])['other_variable'].sum()


# Merging:


# importing the necessary libraries
import pandas as pd

# loading the datasets
data1 = pd.read_csv('data1.csv')
data2 = pd.read_csv('data2.csv')

# merging the two datasets based on a common key
merged_data = pd.merge(data1, data2, on='common_key')

# merging the two datasets based on multiple keys
merged_data2 = pd.merge(data1, data2, on=['key1', 'key2'])



# Finding anomalies:

# importing the necessary libraries
import pandas as pd

# loading the datasets
data1 = pd.read_csv('data1.csv')
data2 = pd.read_csv('data2.csv')

# merging the two datasets based on a common key
merged_data = pd.merge(data1, data2, on='common_key')

# merging the two datasets based on multiple keys
merged_data2 = pd.merge(data1, data2, on=['key1', 'key2'])




# importing the necessary libraries
import pandas as pd
import numpy as np

# loading the dataset
data = pd.read_csv('data.csv')

# calculate z-scores for a numerical variable
data['z_score'] = (data['numerical_variable'] - np.mean(data['numerical_variable'])) / np.std(data['numerical_variable'])

# identify outliers based on z-scores
outliers = data[data['z_score'] > 3]

# calculate percentiles for a numerical variable
percentiles = data['numerical_variable'].quantile([0.25, 0.5, 0.75])

# identify values outside the interquartile range (IQR) for a numerical variable
IQR = percentiles[0.75] - percentiles[0.25]
lower_limit = percentiles[0.25] - 1.5 * IQR
upper_limit = percentiles[0.75] + 1.5 * IQR
outliers2 = data[(data['numerical_variable'] < lower_limit) | (data['numerical_variable'] > upper_limit)]
