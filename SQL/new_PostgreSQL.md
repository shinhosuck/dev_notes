# Install from Ubuntu Repositories:
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

# Log into an iteractive PostgreSQL session:
sudo -u postgres psql

# Create a database for Django project:
CREATE DATABASE blog;

# Create a database user
CREATE USER admin WITH PASSWORD 'march232014';

# Modify connection parameters:
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';

# Give database user access rights to the database:
GRANT ALL PRIVILEGES ON DATABASE blog TO admin;

# Exit SQL prompt
\q

# PostgreSQL Optimization Configuration
https://docs.djangoproject.com/en/4.2/ref/databases/#optimizing-postgresql-s-configuration
