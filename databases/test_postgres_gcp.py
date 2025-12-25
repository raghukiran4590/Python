from google.cloud.sql.connector import Connector
# import pg8000.dbapi

# Define your instance connection name, database credentials, and database name
# It's recommended to store these securely, e.g., in environment variables or a secret manager
INSTANCE_CONNECTION_NAME = "dig-apm1017605-gld-017n:us-east4:gpgsql-apm1017605-00uat01"


DB_USER = "srctopology"
# DB_PASS = "8ZY#REBX3"
DB_NAME = "postgres"

connector = Connector()
conn = connector.connect(
    INSTANCE_CONNECTION_NAME,
    "pg8000",
    user=DB_USER,
    password=DB_PASS,
    db=DB_NAME)

# Example usage:
try:
    with conn.cursor() as cursor:
        cursor.execute("SELECT version();")
        result = cursor.fetchone()
        print(f"PostgreSQL version: {result[0]}")

except Exception as e:
    print(f"Error connecting to Cloud SQL: {e}")