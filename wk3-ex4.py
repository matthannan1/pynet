# IP address validator

import sys
input = sys.argv
print

if len(input) != 2:
    sys.exit("Invalid input. IP address required. Err6")

ip_addr = input[1]
ipList = ip_addr.split(".")

if len(ipList) != 4:
    sys.exit("Invalid input. This is not an IP address. Err A")

if int(ipList[0]) <= 1 or int(ipList[0]) >= 223:
    print ipList[0]
    sys.exit("Invalid input. This is not a valid IP address. Err B")

if int(ipList[0]) == 127:
    sys.exit("Invalid input. IP address can not be in 127.0.0.0 subnet. Err3")

if int(ipList[0]) == 169 and int(ipList[1]) == 254:
    sys.exit("Invalid input. IP address can not be in 169.254.0.0 subnet. Err4")

for i in ipList:
    if int(i) >= 1:
        if int(i) < 0 or int(i) > 255:
            sys.exit("Invalid input. This is not a valid IP address. Err5")

print "IP Address %s is valid.\n" % ip_addr
