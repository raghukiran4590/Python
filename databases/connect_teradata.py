import teradatasql

versionQuery = "SELECT InfoData AS Version FROM DBC.DBCInfoV WHERE InfoKey = 'VERSION'"
databaseQuery = "select trim(a.databasename) databasename from dbc.databasesV a, dbc.diskspaceV b where a.dbkind = 'D' and a.databasename = b.databasename GROUP BY 1 order by 1 "

DB_HOST = "DWPROD1COP1"
DB_USER = "srctopology"
# DB_PASSWORD = "!Jkq8jc-9WvwcmT2kJK!65Z2!"

try:
    conn = teradatasql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, logmech="LDAP")
    print("Connected")
    with conn.cursor() as cursor:
        cursor.execute(versionQuery)
        version = cursor.fetchall()
        print(f"Version : {version}")
        cursor.execute(databaseQuery)
        databases = cursor.fetchall()
        print(f"Databases : ")
        print(databases)

except teradatasql.DatabaseError as e:
    print(f"Database error: {e}")
