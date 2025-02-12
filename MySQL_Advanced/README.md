## MySQL_Advanced

### 1. **How to Create Tables with Constraints in MySQL**

When creating tables in MySQL, you can specify constraints to enforce rules on the data being inserted. The most common constraints are `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `DEFAULT`, and `CHECK`.

**Example:**

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,    -- Primary Key Constraint
    name VARCHAR(100) NOT NULL,            -- NOT NULL Constraint
    email VARCHAR(100) UNIQUE,             -- UNIQUE Constraint
    salary DECIMAL(10, 2) DEFAULT 0.00,    -- DEFAULT Constraint
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id), -- FOREIGN KEY Constraint
    CHECK (salary >= 0)                    -- CHECK Constraint (since MySQL 8.0.16)
);
```

**Explanation of Constraints:**

- **PRIMARY KEY**: Ensures that the column values are unique and not null.
- **FOREIGN KEY**: Enforces a link between two tables by referencing a column in another table.
- **UNIQUE**: Ensures that all the values in a column are unique across the table.
- **NOT NULL**: Ensures that the column cannot contain `NULL` values.
- **DEFAULT**: Assigns a default value if no value is provided.
- **CHECK**: Enforces a condition on the column values.

### 2. **How to Optimize Queries by Adding Indexes**

Indexes improve query performance by allowing the database to find rows more efficiently without having to scan every row in the table. Indexes are typically added to columns that are frequently used in `WHERE` clauses, joins, and sorting operations.

**Creating Indexes:**

```sql
CREATE INDEX idx_employee_name ON employees(name);   -- Index on 'name' column
CREATE UNIQUE INDEX idx_employee_email ON employees(email);  -- Unique Index on 'email'
```

Indexes can be added when creating a table or after a table has been created.

**When to Use Indexes:**

- On columns frequently used in `WHERE` clauses.
- On columns used for joins.
- On columns used in `ORDER BY` or `GROUP BY` clauses.
- Avoid indexing columns with a lot of duplicate values.

**Caveats:**

- Indexes can slow down `INSERT`, `UPDATE`, and `DELETE` operations as the indexes need to be maintained.
- Too many indexes can consume additional disk space.

### 3. **Stored Procedures and Functions in MySQL**

**Stored Procedures** are a set of SQL statements that can be executed on the server. They are used to encapsulate repetitive tasks.

**Creating Stored Procedures:**

```sql
DELIMITER //
CREATE PROCEDURE get_employee(IN emp_id INT)
BEGIN
    SELECT * FROM employees WHERE id = emp_id;
END //
DELIMITER ;
```

- **IN** parameter allows you to pass a value to the procedure.
- **OUT** parameters can be used to return values from the procedure.

**Calling a Stored Procedure:**

```sql
CALL get_employee(1);
```

**Functions** in MySQL are similar to stored procedures, but they return a single value and can be used in SQL expressions.

**Creating Functions:**

```sql
DELIMITER //
CREATE FUNCTION get_salary(emp_id INT) RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE emp_salary DECIMAL(10, 2);
    SELECT salary INTO emp_salary FROM employees WHERE id = emp_id;
    RETURN emp_salary;
END //
DELIMITER ;
```

**Calling a Function:**

```sql
SELECT get_salary(1);
```

### 4. **Views in MySQL**

**Views** are virtual tables based on the result of a `SELECT` query. They are used to simplify complex queries or present data in a different way without affecting the underlying table.

**Creating Views:**

```sql
CREATE VIEW employee_view AS
SELECT id, name, salary FROM employees WHERE salary > 50000;
```

**Using Views:**

```sql
SELECT * FROM employee_view;
```

- Views are useful for security, as you can restrict access to specific columns or rows in a table.
- Views can be updated in some cases, but not all views are updatable (especially those involving joins, aggregation, etc.).

### 5. **Triggers in MySQL**

**Triggers** are special kinds of stored procedures that are automatically executed when certain events occur in the table (like `INSERT`, `UPDATE`, or `DELETE`).

**Creating Triggers:**

```sql
DELIMITER //
CREATE TRIGGER before_insert_employee
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 0 THEN
        SET NEW.salary = 0;   -- Prevent negative salary
    END IF;
END //
DELIMITER ;
```

**Explanation:**

- **BEFORE INSERT**: The trigger runs before a new record is inserted.
- **NEW**: Refers to the new record being inserted (or updated).
- **FOR EACH ROW**: Specifies that the trigger will execute for each row affected by the query.

**Triggers can be used to:**

- Enforce business rules.
- Automatically update other tables.
- Log changes to tables.

**Considerations:**

- Triggers can introduce complexity and make debugging more difficult.
- Overuse of triggers may affect performance, especially when dealing with high-volume transactions.

### Summary

- **Tables with Constraints**: Use constraints like `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, and `CHECK` to enforce data integrity.
- **Indexes**: Optimize query performance by creating indexes on frequently queried columns, but avoid over-indexing.
- **Stored Procedures and Functions**: Encapsulate reusable SQL code into stored procedures (multiple statements) or functions (single return value).
- **Views**: Use views to simplify complex queries or present data in a specific way without altering the base tables.
- **Triggers**: Automatically execute actions before or after certain events like `INSERT`, `UPDATE`, or `DELETE`. Triggers enforce rules or log changes.

Each of these techniques enhances database performance, maintainability, and security when used appropriately.codeelisa@Focus:~/me/MySQL_AdvancedTest$ cd ..
codeelisa@Focus:~/me$ ls
0x0B_redis_basicTest MySQL_AdvancedTest NoSQLTest
codeelisa@Focus:~/me$ cd MySQL_AdvancedTest/
codeelisa@Focus:~/me/MySQL_AdvancedTest$ ls
0-uniq_users.sql 2-fans.sql 4-init.sql 5-init.sql metal_bands.sql
1-country_users.sql 3-glam_rock.sql 4-store.sql README.md my_script.sql
codeelisa@Focus:~/me/MySQL_AdvancedTest$ cat 0-uniq_users.sql
-- bcreate table for users if not exists
CREATE TABLE IF NOT EXISTS users (
id INT NOT NULL AUTO_INCREMENT,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255),
PRIMARY KEY (id)
);
codeelisa@Focus:~/me/MySQL_AdvancedTest$ code .
codeelisa@Focus:~/me/MySQL_AdvancedTest$ ls
0-uniq_users.sql 2-fans.sql 4-init.sql 5-init.sql metal_bands.sql
1-country_users.sql 3-glam_rock.sql 4-store.sql README.md my_script.sql
codeelisa@Focus:~/me/MySQL_AdvancedTest$ cd ..
codeelisa@Focus:~/me$ cd ..
codeelisa@Focus:~$ ls
BackupGraphQL_API atlas-higher_level_programming myStripeProject
Backupatlas-file_manager atlas-smiling-school myStripeProject-HTML
CreateABook atlas-the-joy-of-painting-api myfiles
Docker-the-easy-way atlas-the-joy-of-painting-apiTEST mytest
GraphQL_API atlas-web-development news-scraper
ReactEcommerceStoreWithStripeAPI atlas-web_back_end notes-app
RealityData atlas-web_front_end oklahoma_cooling_centers_python
anaconda3 cardealer-fullstack plantList
apiPlants cssfiles python-object_relational_mapping
atlas-AirBnB_clone fOFB33Ejam2p6qb8wSZ2yWQCAtTdP31JOEi6@github.com reality-check
atlas-AirBnB_clone_jumpstart gardening-shop rewards-app
atlas-AirBnB_clone_v2 holbertonschool-AirBnB_clone t
atlas-AirBnB_clone_v3 holbertonschool-AirBnB_clone_v2 test_programming
atlas-AirBnB_clone_v4 holbertonschool-docker tictactoe
atlas-back-end holbertonschool-smiling-school-javascript win-home
atlas-file-manager holbertonschool-web_front_end
atlas-headphones me
codeelisa@Focus:~$ cd atlas-web-b
-bash: cd: atlas-web-b: No such file or directory
codeelisa@Focus:~$ cd atlas-web_back_end/
codeelisa@Focus:~/atlas-web_back_end$ ls
0x0B_redis_basic Node_JS nodesource_setup.sh python_variable_annotations
Basic_authentication README.md package-lock.json queuing_system_in_js
ES6_basic Session_authentication package.json testing.js
ES6_classes Unittests_and_integration_tests pagination unit_tests
ES6_data_manipulation babel.config.js personal_data unittests_in_js
ES6_promise caching python_async_comprehension
MySql_Advanced node_modules python_async_function
codeelisa@Focus:~/atlas-web_back_end$ mkdir MySQL_Advanced
codeelisa@Focus:~/atlas-web_back_end$ cd MySQL_Advanced/
codeelisa@Focus:~/atlas-web_back_end/MySQL_Advanced$ ls
codeelisa@Focus:~/atlas-web_back_end/MySQL_Advanced$ code .
codeelisa@Focus:~/atlas-web_back_end/MySQL_Advanced$ cd ..
codeelisa@Focus:~/atlas-web_back_end$ cd ..
codeelisa@Focus:~$ cd me
codeelisa@Focus:~/me$ ls
0x0B_redis_basicTest MySQL_AdvancedTest NoSQLTest
codeelisa@Focus:~/me$ cd MySQL_AdvancedTest/
codeelisa@Focus:~/me/MySQL_AdvancedTest$ cat README.md

## MySQL_Advanced

### 1. **How to Create Tables with Constraints in MySQL**

When creating tables in MySQL, you can specify constraints to enforce rules on the data being inserted. The most common constraints are `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `DEFAULT`, and `CHECK`.

**Example:**

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,    -- Primary Key Constraint
    name VARCHAR(100) NOT NULL,            -- NOT NULL Constraint
    email VARCHAR(100) UNIQUE,             -- UNIQUE Constraint
    salary DECIMAL(10, 2) DEFAULT 0.00,    -- DEFAULT Constraint
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id), -- FOREIGN KEY Constraint
    CHECK (salary >= 0)                    -- CHECK Constraint (since MySQL 8.0.16)
);
```

**Explanation of Constraints:**

- **PRIMARY KEY**: Ensures that the column values are unique and not null.
- **FOREIGN KEY**: Enforces a link between two tables by referencing a column in another table.
- **UNIQUE**: Ensures that all the values in a column are unique across the table.
- **NOT NULL**: Ensures that the column cannot contain `NULL` values.
- **DEFAULT**: Assigns a default value if no value is provided.
- **CHECK**: Enforces a condition on the column values.

### 2. **How to Optimize Queries by Adding Indexes**

Indexes improve query performance by allowing the database to find rows more efficiently without having to scan every row in the table. Indexes are typically added to columns that are frequently used in `WHERE` clauses, joins, and sorting operations.

**Creating Indexes:**

```sql
CREATE INDEX idx_employee_name ON employees(name);   -- Index on 'name' column
CREATE UNIQUE INDEX idx_employee_email ON employees(email);  -- Unique Index on 'email'
```

Indexes can be added when creating a table or after a table has been created.

**When to Use Indexes:**

- On columns frequently used in `WHERE` clauses.
- On columns used for joins.
- On columns used in `ORDER BY` or `GROUP BY` clauses.
- Avoid indexing columns with a lot of duplicate values.

**Caveats:**

- Indexes can slow down `INSERT`, `UPDATE`, and `DELETE` operations as the indexes need to be maintained.
- Too many indexes can consume additional disk space.

### 3. **Stored Procedures and Functions in MySQL**

**Stored Procedures** are a set of SQL statements that can be executed on the server. They are used to encapsulate repetitive tasks.

**Creating Stored Procedures:**

```sql
DELIMITER //
CREATE PROCEDURE get_employee(IN emp_id INT)
BEGIN
    SELECT * FROM employees WHERE id = emp_id;
END //
DELIMITER ;
```

- **IN** parameter allows you to pass a value to the procedure.
- **OUT** parameters can be used to return values from the procedure.

**Calling a Stored Procedure:**

```sql
CALL get_employee(1);
```

**Functions** in MySQL are similar to stored procedures, but they return a single value and can be used in SQL expressions.

**Creating Functions:**

```sql
DELIMITER //
CREATE FUNCTION get_salary(emp_id INT) RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE emp_salary DECIMAL(10, 2);
    SELECT salary INTO emp_salary FROM employees WHERE id = emp_id;
    RETURN emp_salary;
END //
DELIMITER ;
```

**Calling a Function:**

```sql
SELECT get_salary(1);
```

### 4. **Views in MySQL**

**Views** are virtual tables based on the result of a `SELECT` query. They are used to simplify complex queries or present data in a different way without affecting the underlying table.

**Creating Views:**

```sql
CREATE VIEW employee_view AS
SELECT id, name, salary FROM employees WHERE salary > 50000;
```

**Using Views:**

```sql
SELECT * FROM employee_view;
```

- Views are useful for security, as you can restrict access to specific columns or rows in a table.
- Views can be updated in some cases, but not all views are updatable (especially those involving joins, aggregation, etc.).

### 5. **Triggers in MySQL**

**Triggers** are special kinds of stored procedures that are automatically executed when certain events occur in the table (like `INSERT`, `UPDATE`, or `DELETE`).

**Creating Triggers:**

```sql
DELIMITER //
CREATE TRIGGER before_insert_employee
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 0 THEN
        SET NEW.salary = 0;   -- Prevent negative salary
    END IF;
END //
DELIMITER ;
```

**Explanation:**

- **BEFORE INSERT**: The trigger runs before a new record is inserted.
- **NEW**: Refers to the new record being inserted (or updated).
- **FOR EACH ROW**: Specifies that the trigger will execute for each row affected by the query.

**Triggers can be used to:**

- Enforce business rules.
- Automatically update other tables.
- Log changes to tables.

**Considerations:**

- Triggers can introduce complexity and make debugging more difficult.
- Overuse of triggers may affect performance, especially when dealing with high-volume transactions.

### Summary

- **Tables with Constraints**: Use constraints like `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, and `CHECK` to enforce data integrity.
- **Indexes**: Optimize query performance by creating indexes on frequently queried columns, but avoid over-indexing.
- **Stored Procedures and Functions**: Encapsulate reusable SQL code into stored procedures (multiple statements) or functions (single return value).
- **Views**: Use views to simplify complex queries or present data in a specific way without altering the base tables.
- **Triggers**: Automatically execute actions before or after certain events like `INSERT`, `UPDATE`, or `DELETE`. Triggers enforce rules or log changes.

Each of these techniques enhances database performance, maintainability, and security when used appropriately.
