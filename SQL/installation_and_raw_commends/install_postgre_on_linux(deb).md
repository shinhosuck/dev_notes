# Postgre installation

project: job_portal
user: job_portal_admin
password: march232014

username: postgres
password: march232014


# Step 1 - Add PostgreSQL Repository

1. Update system:
	- sudo apt update
	- sudo apt install gnupg2 wget nano
	
2. Add the PostgreSQL repository:
	- sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
	
3. Import the repository signing key:
	- curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
	
4. Update the package list:
	- sudo apt update
	
	
# Step 2 - Install PostgreSQL

1. Install PostgreSQL:
	- sudo apt install postgresql-17 postgresql-contrib-17
	
2. Start and enable PostgreSQL service:
	- sudo systemctl start postgresql
	- sudo systemctl enable postgresql
	
	
# Step 3 - Configure PostgreSQL

1. Edit postgresql.conf to allow remote connections by changing listen_addresses to *:
	- sudo nano /etc/postgresql/17/main/postgresql.conf
	- uncomment -> "listen_addresses = '*'"
	
2. Configure PostgreSQL to use md5 password authentication by editing pg_hba.conf,
	this is important if you wish to connect remotely e.g. via PGADMIN :
	- sudo sed -i '/^host/s/ident/md5/' /etc/postgresql/17/main/pg_hba.conf
	- sudo sed -i '/^local/s/peer/trust/' /etc/postgresql/17/main/pg_hba.conf
	- echo "host all all 0.0.0.0/0 md5" | sudo tee -a /etc/postgresql/17/main/pg_hba.conf
	
3. Restart PostgreSQL for changes to take effect:
	- sudo systemctl restart postgresql

4. Allow PostgreSQL port through the firewall:
	- sudo ufw allow 5432/tcp
	
	
# Step 4 - Connect to PostgreSQL

1. Connect as the postgres user:
	- sudo -u postgres psql
	
2. Set a password for postgres user:
	- ALTER USER postgres PASSWORD 'march232014';
	

# Step5 - Create project

1. Create database for the project:
	- CREATE DATABASE myproject;
	
2. Create user and password for the project:
	- CREATE USER myprojectuser WITH PASSWORD 'password';
	
3. Modify connection parameters for the user(job_portal_admin):
	- ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
	- ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
	- ALTER ROLE myprojectuser SET timezone TO 'UTC';
	
4. Grant user(job_portal_admin) the database access rights:
	- GRANT ALL PRIVILEGES ON DATABASE test TO job_portal_admin;
	- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO job_portal_admin;

	* extra permission:
	-- Grant all privileges on all sequences (for auto-incrementing fields)
	- GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO job_portal_admin;
	
	-- Grant all privileges on all functions (e.g., triggers, stored procedures)
	- GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO job_portal_admin;

	* If the data were migrated from Sqlite3, have to give permisson to the tables:
	- ALTER TABLE public.postgresql_car OWNER TO job_portal_admin;
		* "postgresql_car" is the table_name
		* "job_portal_admin" is the username in the settings.py
	
5. Exit PostgreSql:
	- postgres=# \q


# Download pgadmin packages
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" 	> /etc/apt/sources.list.d/pgadmin4.list && apt update'
	
# Install for both desktop and web modes:
sudo apt install pgadmin4

# Install for desktop mode only:
sudo apt install pgadmin4-desktop

# Install for web mode only: 
sudo apt install pgadmin4-web 


























	
	
