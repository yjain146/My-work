# import pandas as pd
# from scipy.stats import skew, kurtosis
# column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
# datae = pd.read_csv(r"C:\Users\yesh\Desktop\Yesh\College\ML\housing.csv",header=None, delimiter=r"\s+", names=column_names)
# summary = datae.describe()
# skewness = datae.apply(skew)
# kurtosis = datae.apply(kurtosis)
# summary.loc['skewness'] = skewness
# summary.loc['kurtosis'] = kurtosis
# print(summary)
# min_values = datae.min()
# max_values = datae.max()
# print("Minimum values:")
# print(min_values)
# print()
# print("Maximum values:")
# print(max_values)

import pandas as pd

# Read the dataset into a DataFrame
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
data = pd.read_csv(r"C:\Users\yesh\Desktop\Yesh\College\ML\housing.csv",header=None, delimiter=r"\s+", names=column_names)
df = pd.DataFrame(data)

# Calculate summary statistics
summary = df.describe()

# Calculate skewness and kurtosis
skewness = df.skew()
kurtosis = df.kurt()

# Print the results
print("Summary Statistics:")
print(summary)
print("\nSkewness:")
print(skewness)
print("\nKurtosis:")
print(kurtosis)

# Calculate the minimum and maximum values
min_values = df.min()
max_values = df.max()

# Print the results
print("Minimum Values:")
print(min_values)
print("\nMaximum Values:")
print(max_values)