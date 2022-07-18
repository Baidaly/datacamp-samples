import os

# Get Environment variables, specify defaults
PHONE_NUMBER = os.environ.get("ALERT_PHONE_NUMBER", None)
RECEIVER = os.environ.get("RECEIVER_NAME", "Random Person")
DEPARTMENT = os.environ.get("DEPARTMENT", "Fleet Department")

# Construct message 
message = """Hello {} from {}!
Here are the speeders:
{}
""".format(RECEIVER, DEPARTMENT, speeders.to_string())

# Send message
sns.publish(PhoneNumber = PHONE_NUMBER, Message = message)