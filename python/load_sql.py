import pandas as pd
import sqlite3

conn = sqlite3.connect("../data/employee.db")

df = pd.read_csv("../data/cleaned_employee.csv")

df.to_sql("employees", conn, if_exists="replace", index=False)

print("Loaded into SQL database")