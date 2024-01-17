-- script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table ( id INT, name VARCHAR(256), score INT );
INSERT INTO second_table (id, name, score) Values (1, "John", 10);
INSERT INTO second_table (id, name, score) Values (2, "Alex", 3);
INSERT INTO second_table (id, name, score) Values (3, "Bob", 14);
INSERT INTO second_table (id, name, score) Values (4, "George", 8);
