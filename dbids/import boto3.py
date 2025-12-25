import boto3
import json

def lambda_handler(event, context):
 try:
  # FOR LIVE VERSION
  message = event['Records'][0]['Sns']['Message']
  print('Stored SNS message from event: ')
  print(message)
  unencryptedImageDetails_dict = json.loads(message)
  print('Turned the JSON message into a dictionary: ')
  print(unencryptedImageDetails_dict)

  # FOR LOCAL LAMBDA TEST VERSION
  # unencryptedImageDetails_dict = event['Records'][0]['Sns']['Message']
  # print(unencryptedImageDetails_dict)

  sns = boto3.client('sns')
  print('Created SNS client.')
  ssm = boto3.client('ssm')
  print('Created SSM client.')
  ec2 = boto3.resource('ec2')
  print('Created EC2 resource.')
  region = boto3.session.Session().region_name
  print('Region Name : ', region)
  session = boto3.client('ec2',region_name=region)
  print('Created EC2 client in ',region )

  storedKey = ssm.get_parameter(Name='/SharedServices/kms/EBSKeyArn')
  print(storedKey)
  KMS_KEY = storedKey['Parameter']['Value']
  print(KMS_KEY)

  imageTags_list = unencryptedImageDetails_dict['Images'][0]['Tags']
  print('Stored snapshot and AMI tags: ')
  print(imageTags_list)

  imageTagsLength = len(imageTags_list)
  print('Stored length of AMI tags list.')
  k = 0

  amiName = ''
  print('Set AMI name to an empty string.')

  print ('Beginning to iterate over tags to find AMI name...')
  k = 0
  while k < imageTagsLength:
    tagKey = imageTags_list[k]['Key']
    if tagKey == 'ImageName':
        print('The AMI name has been found and stored: ')
        amiName = imageTags_list[k]['Value']
        print(amiName)
        break
    k += 1

  unencryptedBlockDeviceMappings_list = unencryptedImageDetails_dict['Images'][0]['BlockDeviceMappings']
  print('Stored unencrypted AMI BlockDeviceMappings: ')
  print(unencryptedBlockDeviceMappings_list)

  unencryptedBlockDeviceMappingsLength = len(unencryptedBlockDeviceMappings_list)
  print('Stored length of BlockDeviceMappings list: ')
  print(unencryptedBlockDeviceMappingsLength)

  encryptedSnapshotIds = []
  print('Created empty list for encrypted snapshot IDs.')

  print('Beginning to iterate through unencrypted EBS BlockDeviceMappings...')
  i = 0
  while i < unencryptedBlockDeviceMappingsLength:
    print('We are on BlockDeviceMapping number: ')
    print(i)
    try:
     unencryptedSnapshotId = unencryptedBlockDeviceMappings_list[i]['Ebs']['SnapshotId']
     print('Stored unencrypted snapshot ID.')
     unencryptedSnapshot = ec2.Snapshot(unencryptedSnapshotId)
     print('Created snapshot object for unencrypted snapshot.')
     try:
        encryptedSnapshotId_dict = unencryptedSnapshot.copy(
            Description='Created from AMIBuilder Lambda function.',
            Encrypted=True,
            KmsKeyId=KMS_KEY,
            SourceRegion='us-east-1'
        )
     except Exception as e:
       print('Exception in unecryptedSnapshot.copy operation with KMS_KEY ', KMS_KEY)
       raise
     print('Copied and encrypted snapshot.')
     encryptedSnapshotId = encryptedSnapshotId_dict['SnapshotId']
     print('Stored encrypted snapshot ID.')
     encryptedSnapshot = ec2.Snapshot(encryptedSnapshotId)
     print('Created snapshot object for encrypted snapshot.')
     print('Waiting until snapshot creation is complete...')
     encryptedSnapshot.wait_until_completed()
     print('Encrypted snapshot creation is complete!')
     encryptedSnapshot_tags = encryptedSnapshot.create_tags(
        Tags=unencryptedImageDetails_dict['Images'][0]['Tags']
     )
     print('Added tags to the encrypted snapshot.')
     encryptedSnapshotIds.append(encryptedSnapshotId)
     print('Appended encrypted snapshot ID to encrypted snapshot ID list.')
     i += 1
    except Exception as e:
     print('Exception in BlockDeviceMappings Iteration ')
     print(e)
     raise

  encryptedSnapshotIdsLength = len(encryptedSnapshotIds)
  print('Stored length of encrypted snapshot ID list: ')
  print(encryptedSnapshotIdsLength)

  print('Beginning to iterate through the list of encrypted snapshot IDs...')
  try:
    j = 0
    while j < encryptedSnapshotIdsLength:
      print('We are on BlockDeviceMapping number: ')
      print(j)
      unencryptedBlockDeviceMappings_list[j]['Ebs']['SnapshotId'] = encryptedSnapshotIds[j]
      print('The snapshot ID has been updated.')
      del unencryptedBlockDeviceMappings_list[j]['Ebs']['Encrypted']
      print('The encryption property in the BlockDeviceMappings list has been removed.')
      j += 1
  except Exception as e:
    Print(' Exception in removing Encrypted property for snapshot...')
    print(e)
    raise

  print('The value of encryptedSnapshotIdsLength is: ')
  print(encryptedSnapshotIdsLength)
  print('The value of unencryptedBlockDeviceMappingsLength: ')
  print(unencryptedBlockDeviceMappingsLength)

  if unencryptedBlockDeviceMappingsLength > encryptedSnapshotIdsLength:
   print('There are still ephemeral storage devices in the BlockDeviceMappings and they will now be removed.')
   while unencryptedBlockDeviceMappingsLength > encryptedSnapshotIdsLength:
    del unencryptedBlockDeviceMappings_list[encryptedSnapshotIdsLength]
    print('An ephemeral storage device has been removed from the BlockDeviceMappings.')
    unencryptedBlockDeviceMappingsLength -= 1
    if encryptedSnapshotIdsLength == unencryptedBlockDeviceMappingsLength:
     print('All ephemeral storage devices have been removed.')

  encryptedBlockDeviceMappings_list = unencryptedBlockDeviceMappings_list
  print('Created a new variable to store the updated BlockDeviceMappings list.')

  rootDeviceName = unencryptedImageDetails_dict['Images'][0]['RootDeviceName']
  print('Stored root device name.')

  try:
    encryptedImageId_dict = ec2.register_image(
          Name=amiName,
          Description='Created from AMIBuilder Lambda function.',
          Architecture='x86_64',
          RootDeviceName=rootDeviceName,
          BlockDeviceMappings=encryptedBlockDeviceMappings_list,
          EnaSupport=True,
          SriovNetSupport='simple',
          VirtualizationType='hvm'
    )
    print('The new AMI has been registered: ')
    print(encryptedImageId_dict)
  except Exception as e:
    print('Exception in ec2.register_image operation')
    print(e)
    raise

  encryptedImage = ec2.Image(encryptedImageId_dict.image_id)
  print('An EC2 Image object has been created using the new AMI ID: ')
  print(encryptedImage)

  encryptedImage.create_tags(
        Tags=unencryptedImageDetails_dict['Images'][0]['Tags']
  )
  print('Tags have been added to the new AMI.')

 except Exception as e:
  print('EXCEPTION *************************************')
  print(e)
  sns = boto3.client('sns')
  print('Created SNS client.')
  sts = boto3.client('sts')
  print('Created STS client.')
  ec2 = boto3.resource('ec2')
  print('Created EC2 resource.')

  accountID = sts.get_caller_identity()['Account']
  print('Stored caller account ID.')

  message = event['Records'][0]['Sns']['Message']
  print('Stored SNS message from event.')

  unencryptedImageDetails_dict = json.loads(message)
  print('Turned the JSON message into a dictionary: ')
  print(unencryptedImageDetails_dict)

  # FOR LOCAL LAMBDA TEST VERSION
  # unencryptedImageDetails_dict = event['Records'][0]['Sns']['Message']
  # print(unencryptedImageDetails_dict)

  imageTags_list = unencryptedImageDetails_dict['Images'][0]['Tags']
  print('Stored snapshot and AMI tags: ')
  print(imageTags_list)

  amiName = ''
  print('Set AMI name to an empty string.')

  print ('Beginning to iterate over tags to find AMI name...')
  k = 0
  while k < imageTagsLength:
    tagKey = imageTags_list[k]['Key']
    if tagKey == 'ImageName':
        print('The AMI name has been found and stored: ')
        amiName = imageTags_list[k]['Value']
        print(amiName)
        break
    k += 1

  snsNotification = sns.publish(
      TargetArn='arn:aws:sns:us-east-1:462968192212:AMIBuilder_ErrorNotification',
      Message='There was an error creating the encrypted AMI in account ' + accountID + ' while attempting to create encrypted AMI ' + amiName
  )

 return 'Encrypted AMI ' + amiName
