import pandas as pd
df=pd.read_csv("C:/Users/shivpoojan mishra/Documents/iris.csv")
print(df.head())
print(df.head)
print(df.describe)
print(df.dtypes)
print(df.isnull().sum())
df = df.drop_duplicates()
print("Remaining rows after dropping duplicates:", len(df))
