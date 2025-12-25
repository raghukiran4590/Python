import cx_Oracle

username = "topology"
# password = "T0pology24!"
server = "topoprd"

# Set the path to the Oracle Instant Client  
cx_path = "/Users/AF35861/Downloads/instantclient_23_3/network/admin" 
  
# Initialize the Oracle client  
if len(cx_path) > 0:  
    cx_Oracle.init_oracle_client(lib_dir=cx_path)
    print("Oracle Client initialized successfully.")

# oracle_dsn = cx_Oracle.makedsn("ihubtopo-d-01.internal.das", 1525, service_name="topod")
# connection = cx_Oracle.connect(user=username, password=password, dsn=oracle_dsn)

connection = cx_Oracle.connect(username, password, server)
print("Connected to Oracle Database.")
db_version = connection.version
print(f"Oracle Database Version: {db_version}")
connection.close()

