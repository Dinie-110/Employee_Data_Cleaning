# Employee Data Cleaning and Analysis (Python, SQL, Excel)
This project demonstrates an end-to-end data analysis workflow involving data cleaning, transformation, storage, and analysis using Python, SQL, and Excel. The objective is to convert raw employee data into a structured, analysis-ready format and generate insights through database queries and spreadsheet analysis.

## Project Structure (Initial Setup)

```
employee-data-cleaning/
│
├── data/                raw_employee.csv
├── python/              clean_data.py, load_sql.py, load_excel.py
├── sql/                 create_table.sql, analysis_queries.sql
└── README.md
```

### Installation

Install required dependency:

```bash
pip install pandas
```

### Running the Project

Navigate to the Python folder:

```bash
cd python
```

Run the data cleaning script:

```bash
python clean_data.py
```

Load cleaned data into the SQL database:

```bash
python load_sql.py
```

Export the data and analysis results to Excel:

```bash
python load_excel.py
```

### Project Structure After Execution

```
employee-data-cleaning/
│
├── data/
│   ├── raw_employee.csv
│   ├── cleaned_employee.csv
│   ├── employee.db
│   └── employee_analysis.xlsx
│
├── python/
│   ├── clean_data.py
│   ├── load_sql.py
│   └── load_excel.py
│
├── sql/
│   ├── create_table.sql
│   └── analysis_queries.sql
│
└── README.md
```

### Running SQL Queries

Move to the data directory where the database is stored:

```bash
cd ../data
```

Open the SQLite database:

```bash
sqlite3 employee.db
```

List available tables:

```sql
.tables
```

Run queries manually or use examples from `analysis_queries.sql`.

Example query:

```sql
SELECT Department, AVG(Salary)
FROM employees
GROUP BY Department;
```

Exit SQLite:

```sql
.quit
```

