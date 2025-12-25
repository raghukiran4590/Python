import boto3
import json

session = boto3.Session(profile_name='aws_config_session')
config_client = session.client('config')

# RDS Query 
with open('./rds_query.txt', 'r') as f:
    rds_query = f.read()

# DynamoDB Query 
with open('./dynamodb_query.txt', 'r') as f:
    dynamodb_query = f.read()

# Redshift Query
with open('./redshift_query.txt', 'r') as f:
    redshift_query = f.read()

rds_response = config_client.select_aggregate_resource_config(
    ConfigurationAggregatorName='aws-controltower-GuardrailsComplianceAggregator',
    Expression=rds_query
)

dynamodb_response = config_client.select_aggregate_resource_config(
    ConfigurationAggregatorName='aws-controltower-GuardrailsComplianceAggregator',
    Expression=dynamodb_query
)

redshift_response = config_client.select_aggregate_resource_config(
    ConfigurationAggregatorName='aws-controltower-GuardrailsComplianceAggregator',
    Expression=redshift_query
)

# Process the results
rds_result = rds_response['Results']
dynamodb_result = dynamodb_response['Results']
redshift_result = redshift_response['Results']
# for resource in resources:
#     print(resource)

with open('rds_config_results.json', 'w') as f:
    json.dump(rds_result, f, indent=4)

with open('dynamodb_config_results.json', 'w') as f:
    json.dump(dynamodb_result, f, indent=4)

with open('redshift_config_results.json', 'w') as f:
    json.dump(redshift_result, f, indent=4)

print("Query results exported to json files")
