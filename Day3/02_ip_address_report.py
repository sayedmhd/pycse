import requests
url = "https://www.virustotal.com/api/v3/ip_addresses/220.77.232.234"
headers = {
    "accept": "application/json",
    "x-apikey": "acd788c76eb01f4a18f180a57c5399c46f4062212c88582a25093bc3d4a063a2"
}
response = requests.get(url, headers=headers)
print(response.text)