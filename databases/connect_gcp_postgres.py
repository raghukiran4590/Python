from google.cloud.sql.connector import Connector
import sqlalchemy

# Database connection details (replace with your actual values)
INSTANCE_CONNECTION_NAME = "dig-apm1017605-gld-017n:us-east4:gpgsql-apm1017605-00uat01"
DB_USER = "srctopology"
# DB_PASS = "8ZY#REBX3"
DB_NAME = "postgres"

# Initialize the Cloud SQL Python Connector
connector = Connector()

# Function to return a database connection object
def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pg8000",  # Specify the database driver
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME,
    )
    return conn

# Create a connection pool using SQLAlchemy
# The 'creator' argument tells SQLAlchemy how to get a new connection
pool = sqlalchemy.create_engine(
    "postgresql+pg8000://",  # Specify the dialect and driver
    creator=getconn,
)

# Example usage:
try:
    with pool.connect() as db_conn:
        # Execute a query
        result = db_conn.execute(sqlalchemy.text("SELECT 1")).scalar()
        print(f"Connection successful! Result: {result}")

        # Example of querying data
        rows = db_conn.execute(sqlalchemy.text("SELECT version()")).fetchall()
        for row in rows:
            print(f"Row: {row}")

except Exception as e:
    print(f"Error connecting to or interacting with the database: {e}")

finally:
    # Close the connector's background resources
    connector.close()