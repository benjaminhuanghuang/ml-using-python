import sklearn
import sklearn
import pandas as pd
import numpy as np


# Load data into DataFrame
data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
col_names = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE", "DIS","RAD","TAX","PTRATIO","B","LSTAT","MEDV"]
df = pd.read_csv(data_url, delimiter=r"\s+", names=col_names)

print(df.head())