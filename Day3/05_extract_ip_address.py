import re
from collections import Counter

def extract_ip_from_logs(log_file):
    with open(log_file, "r") as file:
        log_data =file.read()
    #print(log_data)

    ip_address = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log_data)
    return ip_address

iparray = extract_ip_from_logs("ip_log.txt")

ip_counts = Counter(iparray)

#for ip, count in ip_counts.items():
 #   print(f"IP Address {ip} occurred {count} times.")


high = ip_counts.most_common(3)
print(high)