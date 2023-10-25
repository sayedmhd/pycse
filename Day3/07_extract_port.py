import re
from collections import Counter

def extract_ip_from_logs(log_file):
    with open(log_file, "r") as file:
        log_data =file.read()
    #print(log_data)

    ip_address = re.findall(r"port (\d+)", log_data)
    return ip_address

iparray = extract_ip_from_logs("port.txt")

ip_counts = Counter(iparray)

for ip, count in ip_counts.items():
    print(f" Port {ip} occurred {count} times.")