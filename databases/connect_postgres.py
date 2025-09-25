from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy import text

# Database credentials
user = 'srctopology'
password = '8ZY#REBX3'
host = 'aapsql-10xben-00per01.cdbck5j1ny82.us-east-1.rds.amazonaws.com'
port = '5432'
database = 'postgres'

# Construct the connection string
# 'postgresql+psycopg2' specifies the dialect (PostgreSQL) and the driver (psycopg2)
connection_string = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

# Create the SQLAlchemy engine
try:
    version_query = "SELECT version()"
    dbs_query = "SELECT datname FROM pg_database"
    table_privileges = """select current_database() as database, a.schemaname, a.tablename, b.usename,
                        HAS_TABLE_PRIVILEGE(usename, quote_ident(schemaname) || '.' || quote_ident(tablename), 'select') as has_select,
					    HAS_TABLE_PRIVILEGE(usename, quote_ident(schemaname) || '.' || quote_ident(tablename), 'insert') as has_insert,
					    HAS_TABLE_PRIVILEGE(usename, quote_ident(schemaname) || '.' || quote_ident(tablename), 'update') as has_update,
					    HAS_TABLE_PRIVILEGE(usename, quote_ident(schemaname) || '.' || quote_ident(tablename), 'delete') as has_delete,
					    HAS_TABLE_PRIVILEGE(usename, quote_ident(schemaname) || '.' || quote_ident(tablename), 'references') as has_references
					    from pg_tables a, pg_user b""";
    
    engine = create_engine(connection_string)

    with engine.connect() as connection:
        print("Successfully connected to the PostgreSQL database!")

        version = connection.execute(text(version_query)).scalar()
        print(f"PostgreSQL version: {version}")

        databases = connection.execute(text(dbs_query))
        print(f"PostgreSQL databases : ")
        for db in databases.scalars():
            print(db)
        
        privileges = connection.execute(text(table_privileges))
        print(f"PostgreSQL database privileges : ")
        for row in privileges:
            print(row.database, row.schemaname, row.tablename, row.usename)

except OperationalError as e:
    print(f"Error connecting to the database: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")