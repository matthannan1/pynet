# convert IP to binary

import sys
input = sys.argv
string1 = "IP Address"
string2 = "Binary"

# Master Control
if len(input) != 2:
    sys.exit("Invalid input. Run program again with proper data.")

# Pull IP from argv
ip_addr = input[1]

# Convert IP string to ipList
ipList = ip_addr.split('.')

# Verify IP Address Length
if len(ipList) != 4:
    sys.exit("Invalid IP address.")

# convert octets to Binary
binList = []
for i in ipList:
    binOct = bin(int(i))
    # strip off the 0b, or first two, characters
    binOct = binOct[2:]
    # padding to 8 characters
    while len(binOct) <= 8:
        binOct = '0' + binOct
        # add binOct to list
    binList.append(binOct)

# combine binList elements to binAddy string
binAddy = ".".join(binList)

print
print "%-20s %-20s" % (string1, string2)
print "%-20s %-20s" % (ip_addr, binAddy)
print
