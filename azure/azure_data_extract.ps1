# Connect-AzAccount -DeviceCode
# Set-AzContext -SubscriptionName "CORP-SLVR"
# Update-AzConfig -DefaultSubscriptionForLogin -SubscriptionId "25b174eb-e281-4183-8906-89037a996460"

$DTTM=Get-Date -Format "yyyy_MM_dd"
$JSON_TARGET_DIR="./azure_resource_data_$DTTM/azure_json_files"
$TXT_TARGET_DIR="./azure_resource_data_$DTTM/azure_txt_files"
$ZIP_TARGET_DIR="./azure_resource_data_$DTTM"

New-Item -ItemType Directory -Path $JSON_TARGET_DIR -Force | Out-Null
New-Item -ItemType Directory -Path $TXT_TARGET_DIR -Force | Out-Null
Write-Output "Directories created for JSON and TXT files at $JSON_TARGET_DIR and $TXT_TARGET_DIR"
Write-Output "Azure Data Extract Script Running for $DTTM"

#Generic VMs
Search-AzGraph -Query "resources | where type == 'microsoft.compute/virtualmachines'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/VirtualMachines_$DTTM.json
# SQL VMS
Search-AzGraph -Query "resources | where type == 'microsoft.sqlvirtualmachine/sqlvirtualmachines'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/SQLVirtualMachines_$DTTM.json
# SQL Managed Instances
Search-AzGraph -Query "resources | where type == 'microsoft.sql/managedinstances'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/SQLManagedInstances_$DTTM.json
# SQL Servers
Search-AzGraph -Query "resources | where type == 'microsoft.sql/servers'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/SQLServers_$DTTM.json
# SQL Managed Databases
Search-AzGraph -Query "resources | where type == 'microsoft.sql/managedinstances/databases'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/SQLManagedDatabases_$DTTM.json
# SQL Server Databases
Search-AzGraph -Query "resources | where type == 'microsoft.sql/servers/databases'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/SQLServerDatabases_$DTTM.json
# Flex MySQL
Search-AzGraph -Query "resources | where type == 'microsoft.dbformysql/flexibleservers'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/MySQL_$DTTM.json
# Flex PostgreSQL
Search-AzGraph -Query "resources | where type == 'microsoft.dbforpostgresql/flexibleservers'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/PostgreSQL_$DTTM.json
# Redis Cache
Search-AzGraph -Query "resources | where type == 'microsoft.cache/redis'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/RedisCache_$DTTM.json
# Redis Enterprise
Search-AzGraph -Query "resources | where type == 'microsoft.cache/redisenterprise'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/RedisEnterprise_$DTTM.json
# Cosmos
Search-AzGraph -Query "resources | where type == 'microsoft.documentdb/mongoclusters'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/CosmosDB_$DTTM.json
# DocDB
Search-AzGraph -Query "resources | where type == 'microsoft.documentdb/databaseaccounts'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/DocDB_$DTTM.json
# Cassandra
Search-AzGraph -Query "resources | where type == 'microsoft.documentdb/cassandraclusters'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/Cassandra_$DTTM.json
# Atlas
Search-AzGraph -Query "resources | where type == 'mongodb.atlas/organizations'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/AzureAtlas_$DTTM.json
# Neon
Search-AzGraph -Query "resources | where type == 'neon.postgres/organizations'" | ConvertTo-Json -Depth 100 > $JSON_TARGET_DIR/NeonPostgreSQL_$DTTM.json

Write-Output "Azure Data Extract Completed. JSON files saved to $JSON_TARGET_DIR"
# Copy-Item -Path $JSON_TARGET_DIR/*.json -Destination $TXT_TARGET_DIR

Write-Output "Converting JSON to TXT format."
foreach ($file in Get-ChildItem -Path $JSON_TARGET_DIR/*.json) {
    $content = Get-Content -Path $file.FullName | ConvertFrom-Json
    $txtFileName = [System.IO.Path]::Combine($TXT_TARGET_DIR, [System.IO.Path]::GetFileNameWithoutExtension($file.FullName) + ".txt")
    # $txtFileName = [System.IO.Path]::ChangeExtension($file.FullName, ".txt")
    $content | Out-File -FilePath $txtFileName -Encoding UTF8
}
Write-Output "Converted JSON files to TXT format."
Compress-Archive -Path ./$ZIP_TARGET_DIR -DestinationPath ./$ZIP_TARGET_DIR.zip
Write-Output "Azure Data Extract and Conversion Completed. All files compressed into $ZIP_TARGET_DIR.zip"


