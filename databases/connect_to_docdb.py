import pymongo
from pymongo import MongoClient
# pymongo 4.12.0

'''
For below failure message, there is no issue with DocumentDB connectivity. This error is due to client library version.
What the error means
“Server … reports wire version 7, but this version of PyMongo requires at least 8 (MongoDB 4.2).”
Wire version 7 corresponds to MongoDB 3.4/3.6-era protocol (AWS DocumentDB 3.6 compatibility typically advertises 6–7).
PyMongo 4.x dropped support for servers older than MongoDB 4.0/4.2 (requires wire version ≥ 8).
So your client is too new for your cluster’s protocol.
'''

mongo_user = "SrcTopology"
mongo_pass = "8ZY#REBX3"
# con_str_ver_3 = "adocdb-6225101000-01dev01.cmhzysqbc3y3.us-east-1.docdb.amazonaws.com:37043"
con_str_ver_4 = "adocdb-apm1079217-percl01.cluster-cfrt64dio0wl.us-east-1.docdb.amazonaws.com:27017"
# mongodb://SrcTopology:8ZY%23REBX3@adocdb-nmtest-sit-00dev01.cxxwp8ka8w6i.us-east-2.docdb.amazonaws.com:27017/admin?ssl=true&retryWrites=false&connectTimeoutMS=100000
# con_str_ver_5 = "adocdb-10xben-00sit01.cxxwp8ka8w6i.us-east-2.docdb.amazonaws.com:27017"

# port = ""
ssl_cert = "./global-bundle 1.pem"
users_info = {}

uri = f"mongodb://{mongo_user}:{mongo_pass}@{con_str_ver_4}/?readPreference=nearest&tls=true&tlsCAFile={ssl_cert}&retryWrites=false"
client = MongoClient(uri, serverSelectionTimeoutMS=30000,connectTimeoutMS=30000, socketTimeoutMS=30000)
print("Successfully connected to DocDB Instance")
print(f"version: {pymongo.version}")
print(f"has C extensions: {pymongo.has_c()}")

build_info = client.admin.command("buildinfo")
print(f"build_info : {build_info}")
# databases = client.list_database_names()
databases = client.admin.command({"listDatabases": 1, "nameOnly": "true"})
print(f"databases : {databases}")
# users_info = client.admin.command("usersInfo")
if not users_info:
    print(f"users_info is empty, skipping usersInfo command")
else:
    print(f"users_info : {users_info}")
    print(f"users.info.get('users') : {users_info.get('users', [])}")


