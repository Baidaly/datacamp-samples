'''
You got asked by one of your European coworkers to convert all the speed data coming in to kilometers as part of the lambda transformation function.

For each record coming in, convert the speed to kilometers per hour instead of miles per hour.

The base64 module has been imported for you, and the output empty list is available in your environment.
'''
for record in event['records']:
    #Decode the incoming data and convert it to a list
    payload_dec = base64.b64decode(record['data']).decode().split(" ")
    # Multiply the speed component by 1.60934 to convert to kph
    payload_dec[5] = str(float(payload_dec[5]) * 1.60934)
    # Re-Encode the payload
    payload = " ".join(payload_dec)
    payload_enc = base64.b64encode(payload.encode())
    # Prepare the record
    output.append({
    	'recordId': record['recordId'], 
      	'result': 'Ok', 
        'data': payload_enc,
    })
    
# Return all the records!
print({'records': output})