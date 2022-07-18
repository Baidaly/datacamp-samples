import base64

# Encode string to bytes
incoming_log_encoded = incoming_log.encode()
print(f"String in bytes: \n {incoming_log_encoded} \n")

# Encode bytes to base64
incoming_log_b64 = base64.b64encode(incoming_log_encoded)
print(f"String in b64: \n {incoming_log_b64} \n")

# Decode base64
incoming_log_b64_decoded = base64.b64decode(incoming_log_b64)
print(f"String decoded from b64: \n {incoming_log_b64_decoded} \n")

# Decode bytes to string
print(f"Bytes converted to string:\n {incoming_log_b64_decoded.decode()} \n")