function updateInstanceCloudProvider(instanceName, cloudProvider) {
var instanceRecord = new GlideRecord('cmdb_ci_db_mongodb_instance');
instanceRecord.addQuery('u_instance_name', instanceName);
instanceRecord.query();

if(instanceRecord.next()) {
    if(cloudProvider.toLowerCase().includes('aws')) {
        instanceRecord.u_cloud_provider = 'AWS';
    } else if(cloudProvider.toLowerCase().includes('azure')) {
        instanceRecord.u_cloud_provider = 'AZURE';
    } else if(cloudProvider.toLowerCase().includes('gcp') || cloudProvider.toLowerCase().includes('google')) {
        instanceRecord.u_cloud_provider = 'GOOGLE';
    }
    instanceRecord.update();
    gs.info("Updated instanceName : " + instanceName + " with Cloud Provider: " + cloudProvider);
} else {
    gs.info('No matching instance found for name: ' + instanceName);
}
}

var cloudProvider = "";

//Read the Excel File
var grAttachment = new GlideRecord('sys_attachment');
grAttachment.addQuery('table_name', 'sys_attachment');
// grAttachment.addQuery('table_sys_id', '52a996b3c3d38e585295f49f05013157');
// grAttachment.addQuery('file_name', 'atlas_sample_inventory.xlsx');
grAttachment.addQuery('table_sys_id', '9c505e5d9700fd906bb37b021153afc9');
grAttachment.addQuery('file_name', 'mongodb_atlas_inventory.xlsx');
grAttachment.query();
if (grAttachment.next()) {
    var attachmentSysId = grAttachment.sys_id;
    // gs.info('Attchment SysID : ' + attachmentSysId);
} else {
    gs.info('CSV attachment not found.');
}

//Parse the Excel File
try {
    var gsa = new GlideSysAttachment();
    var attachmentStream = gsa.getContentStream(attachmentSysId);
    var parser = new sn_impex.GlideExcelParser();
    parser.parse(attachmentStream);
    var headers = parser.getColumnHeaders();
    // gs.info('Excel Headers: ' + headers.join(', ')); // To log all headers as a comma-separated string
} catch (e) {
    gs.error('An error occurred: ' + e.message);
}

// Iterate through the rows
while (parser.next()) {
    var updateFlag = false;
    try {
        var rowData = parser.getRow();
        var connectionStrings = rowData['connectionStrings'];
        var parsedObject = JSON.parse(connectionStrings.replace(/'/g, '"'));
        var connectionStringsEntries = parsedObject.privateEndpoint;

        for (var i = 0; i < connectionStringsEntries.length; i++) {
            var entry = connectionStringsEntries[i];
            var endPointEntries = connectionStringsEntries[i].endpoints;
            for (var j = 0; j < endPointEntries.length; j++) {
                var endPointEntry = endPointEntries[j];
                if (endPointEntry.providerName != '') {
                    updateFlag = true;
                    cloudProvider = endPointEntry.providerName;
                    endpointId = endPointEntry.endpointId;
                    var connectionString = entry.srvConnectionString;
                    updateInstanceCloudProvider(connectionString, cloudProvider);
                    if (updateFlag)
                        break;
                }
            }
            if (updateFlag)
                break;
        }
    } catch (e) {
        gs.error('An error occurred: ' + e.message);
    }
}

