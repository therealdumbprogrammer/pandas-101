# 📊 Pandas Cheat Sheet

## 🔍 Introduction
**Pandas** is a powerful and flexible open-source data manipulation and analysis library for Python. It provides data structures and functions needed to work seamlessly with structured data, making it indispensable for data preprocessing, cleaning, and exploratory data analysis in Machine Learning projects.

## 🛠️ Installation

```bash
pip install pandas
```

Or, if using Anaconda:

```bash
conda install pandas
```

## 📦 Importing Pandas

```python
import pandas as pd
```

## 📐 Creating Data Structures

### Series

- **Description:** One-dimensional labeled array capable of holding any data type.

```python
# From a list
s = pd.Series([10, 20, 30, 40])

# From a dictionary
s = pd.Series({'a': 10, 'b': 20, 'c': 30})
```

### DataFrame

- **Description:** Two-dimensional labeled data structure with columns of potentially different types.

```python
# From a dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
```

## 🔑 DataFrame Attributes

```python
print(df.shape)    # Dimensions of the DataFrame
print(df.columns)  # Column names
print(df.index)    # Row indices
print(df.dtypes)   # Data types of columns
```

## ➕➖✖️➗ DataFrame Operations

### Viewing Data

```python
df.head()      # First 5 rows
df.tail(3)     # Last 3 rows
df.info()      # Summary of DataFrame
df.describe()  # Statistical summary
```

### Selecting Data

#### By Column

```python
df['Name']          # Returns a Series
df[['Name', 'Age']] # Returns a DataFrame
```

#### By Row

```python
df.iloc[0]      # First row (integer location)
df.loc[0]       # First row (label)
df.iloc[0:2]    # First two rows
```

#### By Condition

```python
df[df['Age'] > 30]  # Rows where Age > 30
```

## 🔄 Data Manipulation

### Adding/Removing Columns

```python
df['Salary'] = [70000, 80000, 90000]  # Add a new column
df.drop('Salary', axis=1, inplace=True)  # Remove the 'Salary' column
```

### Renaming Columns

```python
df.rename(columns={'Name': 'Full Name'}, inplace=True)
```

### Sorting

```python
df.sort_values(by='Age', ascending=False, inplace=True)
```

### Filtering Data

```python
df_filtered = df[(df['Age'] > 25) & (df['City'] == 'New York')]
```

## 🔧 Handling Missing Values

### Detection

```python
df.isnull().sum()  # Count of missing values per column
df.info()          # Summary including non-null counts
```

### Treatment

```python
df.dropna()        # Drop rows with any missing values
df.fillna(value=0) # Fill missing values with 0
```

## 🔢 Encoding Categorical Variables

### Label Encoding

```python
df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
```

### One-Hot Encoding

```python
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
```

## 📏 Feature Scaling (Using Scikit-learn)

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
```

## 🧮 Grouping and Aggregation

```python
grouped = df.groupby('City')
grouped.mean()  # Mean of numerical columns per city
```

## 🔗 Merging and Joining DataFrames

### Concatenation

```python
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
concatenated = pd.concat([df1, df2], ignore_index=True)
```

### Merging

```python
df1 = pd.DataFrame({'Key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
df2 = pd.DataFrame({'Key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})
merged = pd.merge(df1, df2, on='Key')
```

## 📈 Data Transformation

### Applying Functions

```python
# Apply a function to a column
df['Age'] = df['Age'].apply(lambda x: x + 1)

# Apply a function to the entire DataFrame
df = df.applymap(lambda x: x.upper() if isinstance(x, str) else x)
```

### Pivot Tables

```python
pivot = df.pivot_table(values='Age', index='City', columns='Name', aggfunc='mean')
```

## 🎲 Random Sampling

```python
sample_df = df.sample(n=3)  # Randomly select 3 rows
```

## 📤 Exporting Data

### To CSV

```python
df.to_csv('output.csv', index=False)
```

### To Excel

```python
df.to_excel('output.xlsx', index=False)
```

## 📝 Common Functions

```python
# Unique Values
unique_cities = df['City'].unique()

# Value Counts
city_counts = df['City'].value_counts()

# Checking for Duplicates
duplicate_rows = df[df.duplicated()]
```

## 🧩 Advanced Operations

### Masking and Boolean Indexing

```python
# Create a boolean mask
mask = df['Age'] > 30

# Apply mask to DataFrame
filtered_df = df[mask]
```

### Fancy Indexing

```python
# Select specific indices
indices = [0, 2, 4]
selected_elements = df.iloc[indices]
```

### Conditional Operations

```python
# Replace elements based on condition
df.loc[df['Age'] < 18, 'Category'] = 'Minor'
```

## 🧰 Best Practices

- **Use Vectorized Operations:** Leverage Pandas' optimized functions instead of Python loops for better performance.
- **Chain Methods:** Combine multiple operations in a single line for cleaner code.
  ```python
  df = df.dropna().reset_index(drop=True)
  ```
- **Avoid SettingWithCopyWarning:** Use `.loc` for setting values to prevent unintended side effects.
  ```python
  df.loc[df['Age'] > 30, 'Senior'] = True
  ```
- **Keep Data Clean:** Regularly check for and handle missing values, duplicates, and inconsistent data.
