def is_web_port(port):
    web_ports = [80, 443, 8080]
    return port in web_ports
print(is_web_port(80)) # output: True
print(is_web_port(22)) # output: True


