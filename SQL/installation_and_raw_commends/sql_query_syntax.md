# BASIC COMMANDS

# Definitions:
    

SELECT first_name FROM person
    - 'first_name' -> column name
    - 'person' -> table name or person's name

    ID  FIRST NAME  LAST NAME  AGE
    1   jack        smith      45
    2   greg        young      33
    3   matt        jackson    50
    4   dan         zack       18 

# Keywords:
    - SELECT 
    - FROM
    - ORDER BY,
    - ASC,
    - DESC,
    - DISTINCT,
    - WHERE,
    - AND,
    - OR,
    - LIMIT,
    - OFFSET,
    - FETCH,
    - IN,
    - BETWEEN,
    - LIKE,
    - ILIKE -> case insensitive,
    - GROUP BY,
    - COUNT(),
    - HAVING,
    - MAX(),
    - MIN(),
    - SUM(),
    - AVG(),
    - ROUND(),
    - COALESCE() -> takes 2 args
    - NULLIF() - used with some num / 0
    - NOW() -> current date and time.
    - NOW()::DATE or ::TIME -> current date or time;
    - INTERVAL '2 years' -> NOW() - INTERVAL '2 years'
    - EXTRACT() -> EXTRACT(YEAR FROM NOW()) year, month, day, week, dow, etc...
    - AGE() -> AGE(NOW(), some_date)
    - DELETE,
    - INSERT INTO table_name,
    - VALUES,
    - ADD -> ALTER TABLE table_name ADD CONSTRAINT unique_email UNIQUE (email);
    - UPDATE -> UPDATE person SET first_name = 'Jane' WHERE id = 1;
    - SET,
    - ON CONFLICT (column_name) DO NOTHING -> just does nothing;
    - ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email, last_name = EXCLUDED.first_name, and so forth...
    - JOIN table_name ON -> used with foreign key.
    - IS,
    - NULL,
    - LEFT JOIN

    * when working with IN, use data type tuple ('',)
    Example: SELECT * FROM person WHERE country_of_birth IN ('China', 'France');

    * DISTINCT comes before the column selection 
    Example SELECT DISTINCT first_name FROM

    * COUNT() function comes after the column selection
    Example SELECT first_name, COUNT(*) FROM

    * HAVING comes after GROUP BY and functions such as COUNT() comes after HAVING.




# In most cases sql uses arithmetic and comparison operator.

# Comparison operators
    - <> not equal
    - = equal
    - <= less than or equal
    - >= greater than or equal

# Arithmetic operators

# keyword usage:

1. Select every column:
    - SELECT * FROM person

2. Select random columns:
    - SELECT first_name, last_name, email FROM person

3. ORDER BY keyword:
    * can use ASC or DESC
    - SELECT * FROM person ORDER BY first_name DESC

4. DISTINCT keyword:
    * this does not include duplicate countries
    - SELECT DISTINCT country_of_birth FROM person ORDER BY country_of_birth DESC

5. WHERE keyword:
    * select all columns where row value id equals 1
    - SELECT * FROM person WHERE id=1

6. LIMIT keyword:
    * fetch only 5 rows
    - SELECT * FROM person LIMIT 5;

7. OFFSET keyword:
    * skip 10 rows and then fetch 2 row from the remainder
    - SELECT * FROM person OFFSET 10 LIMIT 2;

8. FETCH keyword:
    * skip 10 rows and then fetch first 2 row only from the remainder
    - SELECT * FROM person OFFSET 10 FETCH FIRST 2 ROWS ONLY;

9. IN keyword:
    - SELECT * FROM person WHERE first_name IN ('Jack', 'James');

10. BETWEEN keyword:
    - SELECT * FROM person WHERE age BETWEEN INT 20 AND 40

11. GROUP BY keyword and COUNT():
    - SELECT country_of_birth, COUNT(*) FROM person GROUP BY country_of_birth;

12. HAVING keyword:
    - SELECT country_of_birth, COUNT(*) FROM person GROUP BY country_of_birth HAVING COUNT(*) >=5 ORDER BY country_of_birth;

13. MAX, MIN, SUM, or AVG with ROUND() comes after SELECT:
    Example: SELECT make, ROUND(MAX(price), 2) FROM car GROUP BY make ORDER BY make;

14. COALESCE() function:
    - SELECT id, first_name, COALESCE(email, 'N/A') FROM person;

15. NULLIF() function, used with COALESCE():
    - SELECT id, product_name, COALESCE(price / NULLIF(0, 0), 'price not available) FROM product;

16. LIKE and ILIKE keyword -> % is a wild card:
    SELECT email FROM person WHERE mail LIKE '%gmail.com';

17. DELETE keyword:
    DELETE FROM person WHERE id=1;

18. UPDATE and SET keyword:
    - UPDATE person SET first_name = 'Jameson' WHERE id=1;

    * Implementing relationship between tables using foreign key concept.
    - UPDATE person SET car_id = 10 WHERE id=2

19. ON CONFLICT keyword:
    - INSERT INTO person (first, last, email) VALUES ('Jack', 'Smith', 'jack@mail.com) ON CONFLICT (email) DO UPDATE SET email = EXCLUDED.first, last = EXCLUDED.last 

20. JOIN ON keywords:
    - SELECT * FROM person JOIN car ON person.car_id = car.id
    * can also manually select columns:
        - SELECT person.first_name, car.make, car.model, car.price FROM person JOIN car ON person.car_id=car.id;

21. LEFT JOIN keyword:
    * pretty much the same as JOIN, just flip the ON person.car_id = car.id to car.id=person.car_id
    * this shows both the person with and without car.
        - SELECT * FROM person LEFT JOIN car ON car.id=person.car_id;

    * this will only show person without car.
        SELECT * FROM person LEFT JOIN car ON car.id = person.car_id WHERE car.id IS NULL;


# Edit and update table

1. Add column:
    - postgres=# ALTER TABLE person
    - postgres=# ADD COLUMN email VARCHAR(100);

2. Update column:
    - postgres=# ALTER TABLE person
    - postgres=# ALTER COLUMN first_name TYPE TEXT;

3. Delete column:
    - postgres=# ALTER TABLE person
    - postgres=# DROP COLUMN email;

4. Create table:
    postgres=# CREATE TABLE person (
        id INT,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        gender VARCHAR(10),
        date_of_birth DATE
    );

5. Insert values:
    - num of columns and values need to match
    - postgres=# INSERT INTO person (
            first_name, 
            last_name,
            gender,
            date_of_birth,
            email 
        )
    - postgres=# VALUES (
            'Jack', 
            'Smith', 
            'Male', 
            DATE '1991-04-10', 
            'jack_smith@mail.com'
        );

6. Delete table:
    - DROP TABLE person;

# copy data to csv file:
- test=# \copy (SELECT * FROM person LEFT JOIN car ON car.id=person_car_id 
ORDER BY car_id FETCH FIRST 4 ROWS ONLY) TO '/home/anderson/Desktop/results.csv'
DELIMITER ',' CSV HEADER;

# Adding extensions:
- check for extensions:
    - SELECT * FROM pg_available_extensions;

- adding extension -> example: uuid-extension:
    - CREATE EXTENSION IF NOT EXISTS 'uuid-ossp';

- run uuid function:
    - SELECT uuid_generate_v4();