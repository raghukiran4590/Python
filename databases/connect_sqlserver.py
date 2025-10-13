import jaydebeapi
import sys

def main():
    try:
        # jTDS Driver name
        driver_name = "net.sourceforge.jtds.jdbc.Driver"

        # jTDS Connection URL format:
        # jdbc:jtds:<server_type>://<server>[:<port>][/<database>][;<property>=<value>[;...]]
        connection_url = "jdbc:jtds:sqlserver://sql-snow-dev.us.ad.wellpoint.com:10002/ServiceNow;domain=us;ssl=required;socketTimeout=20000;usentlmv2=true;"

        # Connection properties (replace with your credentials)
        connection_properties = {
            "user": "snwihub",
            "password": "NqIHNE72wTI!v9hq-!nNCud9H",
            # Optional: Add other jTDS properties as needed, e.g., "domain": "your_domain"
        }

        # Path to the downloaded jTDS JAR file
        jar_path = "/Users/AF35861/Downloads/jtds-1.3.1.jar" # Replace with your actual path

        # Establish connection
        connection = jaydebeapi.connect(driver_name, connection_url, connection_properties, jar_path)
        cursor = connection.cursor()

        # Execute the version query
        cursor.execute("SELECT @@VERSION")

        # Fetch and print the result
        version_info = cursor.fetchone()
        if version_info:
            print(f"SQL Server Version: {version_info[0]}")
        else:
            print("Could not retrieve SQL Server version.")

    except Exception as err:
        print(f"Error connecting to database: {err}")

    finally:
        if 'connection' in locals() and connection:
            connection.close()

if __name__ == "__main__":
    sys.exit(main())