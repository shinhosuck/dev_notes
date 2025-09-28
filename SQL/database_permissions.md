# Grant user(job_portal_admin) the database access rights:

    1. Grant Database Access Rights
    To allow the user job_portal_admin to access the database:

    - GRANT ALL PRIVILEGES ON DATABASE test TO job_portal_admin;

    2. Grant Permissions on All Tables
    To allow job_portal_admin to access all tables in the public schema:

    - GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO job_portal_admin;


    # EXTRA PERMISSIONS:

    3. Grant Permissions on Sequences
    Since PostgreSQL uses sequences for auto-incrementing fields (e.g., primary keys),
    you'll need to grant permission for the user to access and modify sequences:

        - GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO job_portal_admin;

    4. Grant Permissions on Functions
    If your project uses stored procedures or triggers,
    you need to grant permissions on functions (like triggers or any custom functions):

        - GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO job_portal_admin;

    5. Change Ownership of Existing Tables (if migrated from SQLite)
    If the data is migrated from SQLite (or any other system) and the tables were
    created by a different user, you'll need to change the ownership of those tables:

        - ALTER TABLE public.postgresql_car OWNER TO job_portal_admin;

    6. Grant Permissions for Schema Operations
    Django will often need the ability to create tables and perform other operations in the schema.
    To allow this, you must grant schema-related permissions:

        - GRANT USAGE, CREATE ON SCHEMA public TO job_portal_admin;

    7. Change Ownership of the django_migrations Table
    Finally, if the django_migrations table already exists but was created by a different user,
    you’ll need to transfer ownership of the table to the Django user:

        - ALTER TABLE django_migrations OWNER TO job_portal_admin;
