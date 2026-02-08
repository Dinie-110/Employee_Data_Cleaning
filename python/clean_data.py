import pandas as pd

#load raw data
df = pd.read_csv("../data/raw_employee.csv")

#missing age as median
df['Age'] = df['Age'].fillna(df['Age'].median())
#missing age as Unknown
#df['Age'] = df['Age'].fillna('Unknown')


#split department and region
df[['Department', 'Region']] = df['Department_Region'].str.split('-', expand=True)

#standardize join date
df['Join_Date'] = pd.to_datetime(df['Join_Date'])

#remove duplicates
df = df.drop_duplicates(subset=['Employee_ID'])

#round salary
df['Salary'] = df['Salary'].round(2)

#save cleaned data
df.to_csv("../data/cleaned_employee.csv", index=False)

print("Data cleaned and saved")