import re
from collections import Counter

def extract_ip_from_logs(log_file):
    with open(log_file, "r") as file:
        log_data =file.read()
    #print(log_data)

    user = re.findall(r"user[=| ](\w+)", log_data)
    return user

userarray = extract_ip_from_logs("Linux_2k.log")

ip_counts = Counter(userarray)

for user, count in ip_counts.items():
    print(f" {user} ")


high = ip_counts.most_common(100)
print(high)