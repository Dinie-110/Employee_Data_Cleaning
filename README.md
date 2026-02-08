# Employee Data Cleaning and Analysis (Python, SQL, Excel)
This project demonstrates an end-to-end data analysis workflow involving data cleaning, transformation, storage, and analysis using Python, SQL, and Excel. The objective is to convert raw employee data into a structured, analysis-ready format and generate insights through database queries and spreadsheet analysis.

starting with

employee-data-cleaning/

│

├── data/                raw_employee.csv

├── python/              clean_data.py and load_sql.py and load_excel.py

├── sql/                 create_table.sql and analysis_queries.sql

└── README.md


in bash

pip install pandas

cd python

python clean_data.py

python load_sql.py

python load_excel.py


then you will get


employee-data-cleaning/

│

├── data/                raw_employee.csv and cleaned_employee.csv and employee.db and employee_analysis.xlsx

├── python/              clean_data.py and load_sql.py and load_excel.py

├── sql/                 create_table.sql and analysis_queries.sql

└── README.md


to run query in employee database


cd ../data

sqlite3 employee.db

.tables

#promt query as wanted or can use example in analysis_queries.sql one by one

SELECT Department, AVG(Salary)

FROM employees

GROUP BY Department;

