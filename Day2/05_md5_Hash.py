import hashlib
def generat_md5(data):
    return hashlib.md5(data.encode()).hexdigest()
print(generat_md5("P@ssw0rd"))