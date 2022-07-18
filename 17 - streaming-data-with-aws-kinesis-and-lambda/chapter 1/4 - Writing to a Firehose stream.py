# OBD2_sensors.py: Write to Firehose stream. EDIT HERE.
import _setup, create_firehose
firehose, s3, records = _setup.ex_vars
for idx, row in records.iterrows(): 

    # Create a payload string that ends with a newline
    payload = ' '.join(str(value) for value in row) 
    payload = payload + "\n"
    print("Sending payload: {}".format(payload))

    # Send the payload string to Firehose stream
    res = firehose.put_record(
        DeliveryStreamName = 'gps-delivery-stream',
        Record = {'Data': payload})

    # Print the written RecordId
    print("Wrote to RecordId: {}".format(res['RecordId']))
