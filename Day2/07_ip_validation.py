import ipaddress

def validate_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False
    
print(validate_ipv4("192.168.1.1"))
print(validate_ipv4("255.255.255.256"))