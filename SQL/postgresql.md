# Install PostgreSql
sudo apt-get install postgresql postgresql-contrib

# Install psycopg2
pip install psycopg2-binary

# Connect to sql
sudo -s
su postgres
psql

# Create a user
https://www.postgresql.org/docs/8.0/sql-createuser.html

CREATE USER davide WITH PASSWORD 'jw8s0F4';

# Exit from sql
\q

# Exit from root@ user status
control + D

