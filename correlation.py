import pandas as pd
import numpy as np
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
datae = pd.read_csv(r"C:\Users\yesh\Desktop\Yesh\College\ML\housing.csv",header=None, delimiter=r"\s+", names=column_names)
print(datae.head())
print(datae[['LSTAT', 'MEDV']].corr())
print(datae[['AGE', 'TAX']].corr())