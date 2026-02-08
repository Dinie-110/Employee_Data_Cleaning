-- Average salary per department
SELECT Department, AVG(Salary)
FROM employees
GROUP BY Department;

-- Remote workers count
SELECT Remote_Work, COUNT(*)
FROM employees
GROUP BY Remote_Work;

-- Top performers
SELECT *
FROM employees
WHERE Performance_Score = 'Excellent';

-- Employees per region
SELECT Region, COUNT(*)
FROM employees
GROUP BY Region;