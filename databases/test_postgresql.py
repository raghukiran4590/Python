import psycopg2

# postgres_conn_list = ["aapsql-apm1009822-00dev01.c8acin23yz5j.us-east-2.rds.amazonaws.com",
#                       "aapsql-apm1006139-00dev01.cmbfpqectret.us-east-2.rds.amazonaws.com",
#                       "aapsql-apm1046115-00per01.crg4myqkiwvr.us-east-1.rds.amazonaws.com",
#                       "aapsql-apm1046115-00uat01.crg4myqkiwvr.us-east-1.rds.amazonaws.com",
#                       "aapsql-apm1046115-00per01.crg4myqkiwvr.us-east-1.rds.amazonaws.com",
#                       "aapsql-apm1009560-00dev01.cxxwp8ka8w6i.us-east-2.rds.amazonaws.com",
#                       "aapsql-apm1008473-00sit01.cxxwp8ka8w6i.us-east-2.rds.amazonaws.com"
#                       ]

postgres_conn_list = ["dig-apm1017605-gld-017n.us-east4.gpgsql-apm1017605-00uat01"]

# Connection parameters
DB_NAME = "postgres"
DB_USER = "srctopology"
# DB_PASSWORD = "8ZY#REBX3"
DB_PORT = 5432

# print("Reading through the postgresql connection list in a for loop:")

for item in postgres_conn_list:
    try: 
        # print("Connecting to : "+item)

        conn = psycopg2.connect(
        host=item,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
        )

        print("Connected to : "+item)

        # Create a cursor object to execute SQL commands
        cur = conn.cursor()

        # Example: Execute a query
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print(f"PostgreSQL database version: {db_version[0]}")

        # Close the cursor and connection
        cur.close()
        conn.close()
        # print("Connection closed.")

    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")