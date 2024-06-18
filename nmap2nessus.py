import re

file1 = open("nmap.txt", "r")
file1lines = file1.readlines()
ip = ""
print("Host,Port")
for line in file1lines:
    if "Nmap scan report for" in line:
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)[0]
        continue
    elif "/" in line and "open" in line:
        port = line.split("/")[0]
        print('"{0}","{1}"'.format(ip, port))
