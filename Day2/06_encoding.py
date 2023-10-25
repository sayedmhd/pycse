import base64
def encode_base64(data):
    return base64.b64encode(data.encode()).decode()
def decode_base64(data):
    return base64.b64decode(data.encode()).decode()

encoded = encode_base64("secret")
print(encoded) # outputs: c2VjcmV0

decode = decode_base64(encoded)
print(decode) # outputs : secret