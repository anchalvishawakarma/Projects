Project: SQL Query Solutions for Employee and Client Data Analysis

Overview

This project involves writing SQL queries to address various business questions related to employees, branches, clients, and suppliers in an organization. The goal is to extract meaningful insights from the database to support decision-making processes. The queries focus on tasks such as calculating salaries, counting clients, retrieving employee details, and analyzing sales data.

Project Details
Maximum Salary among Female Employees in the Corporate Branch

Objective: Identify the highest salary earned by female employees in the "Corporate" branch.
Query:
sql
Copy code
SELECT branch_name 'Branch', MAX(salary) 'Salary' 
FROM employees e1 
INNER JOIN branches b1 ON e1.branch_id = b1.branch_id 
WHERE sex = 'F' AND branch_name = 'Corporate';
Employee Details with Client Count for High Earners

Objective: Retrieve employee details along with the count of clients they work with, focusing on employees with salaries greater than $50,000.
Queries:
sql
Copy code
SELECT emp_id, first_name, last_name, birth_date, sex, salary, super_id, e1.branch_id, COUNT(client_id) 
FROM employees e1 
INNER JOIN clients c1 ON e1.branch_id = c1.branch_id 
WHERE salary > 50000;
sql
Copy code
SELECT emp_id, first_name, last_name, birth_date, sex, salary, super_id, e1.branch_id, client_id 
FROM employees e1 
INNER JOIN clients c1 ON e1.branch_id = c1.branch_id 
WHERE salary > 50000;
Average Salary of Male Employees in the Scranton Branch

Objective: Calculate the average salary of male employees in the "Scranton" branch.
Query:
sql
Copy code
SELECT AVG(salary) 
FROM employees e1 
INNER JOIN branches b1 ON e1.branch_id = b1.branch_id 
WHERE sex = 'M' AND branch_name = 'Scranton';
Client Count per Branch with a Minimum of 5 Clients

Objective: Retrieve the count of clients for each branch where the count is greater than 5.
Query:
sql
Copy code
SELECT COUNT(*) 
FROM clients 
GROUP BY branch_id 
HAVING COUNT(*) > 5;
Total Sales by Employees in the Corporate Branch

Objective: Find the total sales made by each employee in the "Corporate" branch with sales exceeding $100,000.
Query:
sql
Copy code
SELECT total_sales 
FROM sales s 
INNER JOIN branches b 
INNER JOIN employees e ON e.emp_id = s.emp_id = b.mgr_id 
GROUP BY branch_name 
HAVING branch_name = 'Corporate';
Total Sales for Each Client in the Corporate Branch

Objective: Retrieve the total sales for each client in the "Corporate" branch.
Query:
sql
Copy code
SELECT client_id, total_sales 
FROM sales s 
INNER JOIN branches b ON mgr_id = emp_id 
WHERE branch_name = 'Corporate' 
GROUP BY client_id;
Details of Female Employees with Salary above $70,000

Objective: Retrieve details of female employees with a salary above $70,000.
Query:
sql
Copy code
SELECT * 
FROM employees 
WHERE sex = 'F' AND salary > 70000;
Clients with Names Starting with 'T'

Objective: Find the clients whose names start with 'T'.
Query:
sql
Copy code
SELECT client_name 
FROM clients 
WHERE client_name LIKE 'T%';
Employees Sorted by Salary in Descending Order

Objective: Get the names of employees sorted by their salary in descending order.
Query:
sql
Copy code
SELECT first_name, last_name 
FROM employees 
ORDER BY salary DESC;
Clients Sorted Alphabetically by Their Names

Objective: Retrieve a list of clients sorted alphabetically by their names.
Query:
sql
Copy code
SELECT client_name 
FROM clients 
ORDER BY client_name;


Additional Queries
Highest Sales per Client
Employees with Last Names Ending in 'son'
Supplier Names Containing 'Paper'
Employees' Salaries in Ascending Order
Branch Names in Alphabetical Order
Supplier Names and Supply Types by Supply Types
Average Salary for Each Gender
Number of Clients per Branch
Maximum Total Sales per Client
Branch Names and Employee Counts
Number of Clients per Employee
Average Birth Year per Branch


Conclusion
The SQL queries provided in this project cover a range of data retrieval, aggregation, and filtering tasks, enabling the extraction of insights necessary for business analysis and decision-making.