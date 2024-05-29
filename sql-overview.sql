-- Tables Definition
Table A
id	name
1	Alice
2	Bob
3	Carol

Table B
id	age
1	25
2	30
4	35

-- Types of Joins

-- Inner Join: Returns records with matching values in both tables. It combines rows from two tables based on a common column.
SELECT columns
FROM table1
INNER JOIN table2 ON table1.common_column = table2.common_column;

SELECT A.id, A.name, B.age
FROM A
INNER JOIN B ON A.id = B.id;

Result
id	name	age
1	Alice	25
2	Bob	    30


-- Left (Outer) Join: Returns all records from the left table and matched records from the right table. Unmatched records from the right table will be NULL.
SELECT columns
FROM table1
LEFT JOIN table2 ON table1.common_column = table2.common_column;

SELECT A.id, A.name, B.age
FROM A
LEFT JOIN B ON A.id = B.id;

Result
id	name	age
1	Alice	25
2	Bob	    30
3	Carol	NULL


-- Right (Outer) Join: Returns all records from the right table and matched records from the left table. Unmatched records from the left table will be NULL.
SELECT columns
FROM table1
RIGHT JOIN table2 ON table1.common_column = table2.common_column;

SELECT A.id, A.name, B.age
FROM A
RIGHT JOIN B ON A.id = B.id;

Result
id	    name	age
1	    Alice	25
2	    Bob	    30
NULL	NULL	35

-- Full (Outer) Join: Returns all records when there is a match in either left or right table.
SELECT columns
FROM table1
FULL OUTER JOIN table2 ON table1.common_column = table2.common_column;

SELECT A.id, A.name, B.age
FROM A
FULL OUTER JOIN B ON A.id = B.id;

Result
id	    name	age
1	    Alice	25
2	    Bob	    30
3	    Carol	NULL
NULL	NULL	35

-- Cross Join: Returns the Cartesian product of the two tables (all possible combinations).
SELECT columns
FROM table1
CROSS JOIN table2;

SELECT A.id AS a_id, A.name, B.id AS b_id, B.age
FROM A
CROSS JOIN B;

Result
a_id	name	b_id	age
1	    Alice	1	    25
1	    Alice	2	    30
1	    Alice	4	    35
2	    Bob	    1	    25
2	    Bob	    2	    30
2	    Bob	    4	    35
3	    Carol	1	    25
3	    Carol	2	    30
3	    Carol	4	    35

-- Best Practices
-- Understand the Data: Know your data schema, relationships, and indexes. This helps in writing efficient queries.

-- Select Only Needed Columns: Avoid using SELECT *. Instead, specify only the columns you need.
SELECT column1, column2
FROM table;

-- Use Aliases for Readability: Use table aliases to make your queries more readable.
SELECT t1.column1, t2.column2
FROM table1 t1
INNER JOIN table2 t2 ON t1.common_column = t2.common_column;

-- Filter Early with WHERE: Use the WHERE clause to filter data early in the query process.
SELECT column1, column2
FROM table
WHERE condition;

-- Limit Results: Use LIMIT to restrict the number of rows returned.
SELECT column1, column2
FROM table
LIMIT 10;

-- Optimize Joins: Ensure appropriate indexes are created on columns used in joins. Avoid joining large tables without indexes.
-- Avoid Subqueries When Possible: Use joins instead of subqueries for better performance.

-- Instead of this subquery
SELECT column1
FROM table1
WHERE column2 IN (SELECT column2 FROM table2);

-- Use this join
SELECT t1.column1
FROM table1 t1
INNER JOIN table2 t2 ON t1.column2 = t2.column2;

-- Use Indexes Wisely: Index columns that are frequently used in WHERE clauses, join conditions, and as primary keys.
-- Analyze and Tune Queries: Use EXPLAIN to analyze the query execution plan and identify bottlenecks.

EXPLAIN SELECT column1, column2
FROM table
WHERE condition;

-- Avoid Redundant Data: Normalize your database to eliminate redundant data and ensure data integrity.







