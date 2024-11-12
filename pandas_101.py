import pandas as pd

df = pd.read_csv("train.csv")

print("Head---")
print(df.head())
print("Tail---")
print(df.tail())
print("Info---")
print(df.info())
print("Describe---")
print(df.describe())

df_selected_cols = df[['PassengerId', 'Age']]
print("Selected specific columns---")
print(df_selected_cols.head())

print("Total NA cols---")
print(df.isna().sum())
print("Total Null cols---")
print(df.isnull().sum())

print("Filling Age column---")
df['Age'].fillna(df["Age"].median(), inplace=True)
print(df.isna().sum())

print("Sex before--")
print(df['Sex'])
print("Sex After--")
print(df['Sex'].map({'male': 1, 'female': 0}))

print("Mean age grouped by Passenger class---")
print(df.groupby('Pclass')['Age'].mean())

print("Filtering data --> passengers with age > 30")
df_age_thirty = df[df["Age"] > 30]
print(df_age_thirty[['Name', 'Age']])