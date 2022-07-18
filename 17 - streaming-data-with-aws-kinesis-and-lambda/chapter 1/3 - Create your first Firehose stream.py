# _setup.py: Create clients, load data, etc. No need to edit.

import boto3

# Create firehose client
firehose = boto3.client('firehose', 
    aws_access_key_id="None", 
    aws_secret_access_key="None", 
    region_name='us-east-1', 
    endpoint_url="http://localhost:4573")

# Create s3 client
s3 = boto3.client('s3', 
    aws_access_key_id="None", 
    aws_secret_access_key="None", 
    region_name='us-east-1', 
    endpoint_url="http://localhost:4572")

# Prep variables for export
ex_vars = [firehose, s3]


# create_firehose.py: Create firehose stream. No need to edit.
import _setup
firehose, s3 = _setup.ex_vars

# Create s3 bucket
s3.create_bucket(Bucket='sd-vehicle-data')

# Create Firehose delivery stream
res = firehose.create_delivery_stream(
    DeliveryStreamName="gps-delivery-stream",
    DeliveryStreamType="DirectPut",
    # Specify configuration of the destination S3 bucket
    S3DestinationConfiguration = {
        "BucketARN": "arn:aws:s3:::sd-vehicle-data",
        "RoleARN": "arn:aws:iam::0000000:role/firehoseDeliveryRole"
    })
    
# Print the stream ARN
print("Created Firehose Stream ARN: {}".format(res['DeliveryStreamARN']))
