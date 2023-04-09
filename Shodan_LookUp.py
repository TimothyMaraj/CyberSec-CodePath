import requests
import json 

# script 
with open("ip.txt","r") as file:
    ip_list = file.readlines()

ip_list = [ip.strip() for ip in ip_list]
json_list = []
url = 'https://internetdb.shodan.io/'

for ip in ip_list:
    new_url = url + f"{ip}" 
    json_list.append(requests.get(new_url).json())
    try:
        print("Host(s): ",requests.get(new_url).json()['hostnames'],'\n')
        print("Vulnerabilities: ",requests.get(new_url).json()['vulns'],'\n')
    except:
        print("IP Yields No Data. Starting Next", "\n")


