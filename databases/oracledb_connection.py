import oracledb

# Enable Thick Mode by initializing the Oracle Client with the library directory
oracledb.init_oracle_client(lib_dir="/Users/AF35861/Downloads/instantclient_23_3")

try:
    connection = oracledb.connect(
        user="topology",
        # password="T0pology24!",
        dsn="topoprd"
    )
    print("Successfully connected to Oracle Database in Thick Mode.")

except oracledb.Error as e:
    print(f"Error connecting to Oracle Database: {e}")
finally:
    if 'connection' in locals() and connection:
        connection.close()
        print("Connection closed.")
