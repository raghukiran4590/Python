import oracledb

username = "wdbs"
# password = "YBkHzLmvsQG-n3rTUOpCdAfW$"
dsn = "topod"
tns_admin_dir = "/Users/AF35861/Downloads/instantclient_23_3/network/admin"

# Initialize the Oracle client  
if len(tns_admin_dir) > 0:  
    oracledb.init_oracle_client(lib_dir=tns_admin_dir)
    print("Oracle Client initialized successfully.")

connection = oracledb.connect(user=username, password=password, dsn=dsn)
print("Successfully connected to Oracle Database!")

try:
    # Now you can create a cursor and execute SQL queries
    with connection.cursor() as cursor:
        cursor.execute("SELECT sysdate FROM dual")
        for row in cursor:
            print(f"Current date from database: {row[0]}")

except oracledb.Error as e:
    error_obj, = e.args
    print(f"Error connecting to Oracle Database: {error_obj.message}")

