import pandas as pd
import sqlite3

# connect to database
conn = sqlite3.connect("../data/employee.db")

# load tables
cleaned_df = pd.read_sql("SELECT * FROM employees", conn)
raw_df = pd.read_csv("../data/raw_employee.csv")

# example SQL analysis result
salary_dept = pd.read_sql("""
SELECT Department, AVG(Salary) as Avg_Salary
FROM employees
GROUP BY Department
""", conn)

# export to Excel
with pd.ExcelWriter("../data/employee_analysis.xlsx") as writer:
    raw_df.to_excel(writer, sheet_name="raw_data", index=False)
    cleaned_df.to_excel(writer, sheet_name="cleaned_data", index=False)
    salary_dept.to_excel(writer, sheet_name="salary_analysis", index=False)

print("Excel file created: employee_analysis.xlsx")