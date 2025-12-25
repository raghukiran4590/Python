import mysql.connector

mysql_conn_list = ["aamsql-apm1012279-devcl01.cluster-cfmqwue40p6s.us-east-2.rds.amazonaws.com",
                    "aamsql-apm1000889-00per01.cbmw6tmdk35w.us-east-1.rds.amazonaws.com",
                    "application-autoscaling-82b801d0-fd86-45ff-8833-362df8c1dba8.cmbfpqectret.us-east-2.rds.amazonaws.com",
                    "aamsql-apm1012230-00uat01.clndwnxheovb.us-east-1.rds.amazonaws.com",
                    "aapsql-apm1009560-00dev01.cxxwp8ka8w6i.us-east-2.rds.amazonaws.com",
                    "aapsql-apm1009560-devcl01.cluster-cxxwp8ka8w6i.us-east-2.rds.amazonaws.com"]
        
print("Reading through the mysql connection list in a for loop:")

for item in mysql_conn_list:
    try: 
        print("Connecting to : "+item)

        connection = mysql.connector.connect(
            host=item,
            user="srctopology",
            # password="L@18!mr35lm98",
            database="mysql"
        )
        if connection.is_connected():
            print(item + " - Connected successfully!") 

        if 'connection' in locals() and connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone();
            print(version)

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        