print("""
----------------------
RESIST SOCIETY SCRIPT
THIS IS A DDOS ATTACK SCRIPT
----------------------""")
input('[1]Contunie::')
import os
input('WEB IP////')
ip_list = ['8.8.8.8']
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 100" in response:
        print(f"UP {ip} Ping Successful")
    else:
        print(f"DOWN {ip} Ping Unsuccessful")
