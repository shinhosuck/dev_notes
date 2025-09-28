# Terminal commands

# note:
    psql -> is the sql terminal

1. Log into sql:

    # login as databse superuser:
    * you are only database admin
    - sudo -u postgres psql

    # login as both database and frontend admin:
    * you can make data migrations to specific database_name
    - psql -U postgres database_name


2. Create database:
    - postgres=# CREATE DATABASE database_name;
        - database name is usually project name

3. Restart sql:
    - sudo systemctl restart postgresql

4. Quit out of psql:
    - postgres=# \q

5. Help within psql:
    -  postgres=# help

6. Help within Ubuntu terminal:
    - psql --help

7. Connect remotely:
    - psql -h localhost -p 5432 -U postgres job_portal
        - psql, host(ip), port, username, database_name/project_name

8. Connecting to database within psql:
    - postgres=# /c database_name

9. Clear psql terminal:
    - postgres=# \! clear

10. Delete a database:
    postgres=# DROP DATABASE test;

11. Show description of the table:
    - postgres=# \d -> show conmprehensive list of tables
    - postgres=# \d person -> shows comprehensive list of a single table

12. Delete a table:
    postgres=# DROP TABLE person;

13. Create table:
    postgres=# CREATE TABLE person (
        id INT,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        gender VARCHAR(10),
        date_of_birth DATE
    );

14. Show just the simple tables in a specfi database/database_name:
    test=# \dt 

15. Change to different database:
    postgres=# \c test -> change to dabase test -> test=#

16. Expand table disply -> makes it more readable
    - postgres=# \x

<!-- 14. Add data:
    INSERT INTO person(
        first_name,
        last_name,
        gender,
        date_of_birth
    );
    VALUES (
        'Jack',
        'Smith',
        'Male',
        '1973-10-13'
    ) -->

# Column properties:
    - NOT NULL
    - BIGSERIAL
    - VARCHAR(100)
    - INT,
    - BIGINT
    - DATE
    - DATETIME,
    - TIMESTAMP,
    - default CURRENT_TIMESTAMP,
    - UNIQUE,
    - CHECK,
    - REFERENCES table_name (column),
    - FOREIGN KEY,

