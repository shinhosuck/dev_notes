# Sqlite to PostgreSql

# Commends and steps:

1. Dump existing data to json file: 
    - python3 manage.py dumpdata > datadump.json

    * you can specify the database as well:
        - python manage.py dumpdata --database=your_database_name > datadump.json


2. Update the settings.py:
    Example:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'test',
                'USER': 'postgres',
                'PASSWORD': 'march232014',
                'HOST': 'localhost',
                'PORT': '5432'
            }
        }

3. Add postgres to INSTALLED_APPS:
    'django.contrib.postgres'

4. Run migrate to sync to postgres:
    - python3 manage.py migrate -> migrate to the 'default' database

    * specify database on 2 or more database:
        - python3 manage.py migrate --database=postgres -> migrate to the 'postgres' database

5. Load data to postgres:
    - python3 manage.py loaddata data.json

    * specify database on 2 or more database:
        - python3 manage.py loaddata data.json --database=postgres


NOTE:
    Above steps is only applicable when migrating over to postgres.
    On a fresh project just implemnt step 2 and 3.