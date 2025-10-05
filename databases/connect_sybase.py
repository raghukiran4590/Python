import pyodbc
import datetime

# Connection details
user = "srctopology"
# passwd = "HZXzR5lwFzp9WpKueqB7AHh2g"
host = "va10n10040.WELLPOINT.COM"
# db = "your_database_name"
port = "32025"
# driver = "Adaptive Server Enterprise" Or "FreeTDS" or another appropriate driver
driver = "FreeTDS"

# tsql -H va10n10040.WELLPOINT.COM -p 32025 -U srctopology -P HZXzR5lwFzp9WpKueqB7AHh2g

try:
    print(datetime.datetime.now())
    conn = pyodbc.connect(
        driver=driver,
        server=host,
        # database=db,
        port=port,
        uid=user,
        pwd=passwd
    )
    print("Connection successful!")
    print(conn)

    cursor = conn.cursor()

    # Example query
    query = "SELECT @@version AS version"
    cursor.execute(query)
    row = cursor.fetchall()
    print(f"Result of query: {row}")

except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    print(f"Connection failed: {sqlstate}")
    print(ex)

finally:
    if 'conn' in locals() and conn:
        conn.close()
        print("Connection closed.")