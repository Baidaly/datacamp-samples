# Initialize boto3 session
session = boto3.Session(aws_access_key_id = AWS_KEY_ID, 
    				 aws_secret_access_key = AWS_SECRET, 
                     region_name="us-east-1")

# Read all records in the speeders folder
speeders_total = wr.s3.read_csv('s3://sd-vehicle-data/speeders', 
                                boto3_session = session, 
                                delimiter=" ")

# Write aggregated speeders file
wr.s3.to_csv(df = speeders_total, 
             boto3_session=session, 
             path="s3://sd-vehicle-data/speeders-full/full.csv")