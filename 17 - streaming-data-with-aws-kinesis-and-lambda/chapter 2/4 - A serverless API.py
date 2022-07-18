import boto3

lambda_client = boto3.client('lambda', aws_access_key_id="12345",
    aws_secret_access_key="12345",
    region_name='us-east-1',
    endpoint_url="http://localhost:4574")

def trigger_full_report_builder(event, context):
    async = event['queryStringParameters']['async']
    if async == 'true':
        exec_type = 'Event'
    else:
        exec_type = 'RequestResponse'
        
    result = lambda_client.invoke(
      FunctionName='fullReportBuilder',
      InvocationType=exec_type)
    
    return {
        'statusCode': 200,
        'headers': {
            "content-type" : "application/json"
        },
        'body': "Successfully Invoked"
    }