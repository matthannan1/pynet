print

ipNetAddy = raw_input("IP Network Address: ")
ipNetAddyList = ipNetAddy.split(".")
string1 = "NETWORK_NUMBER"
string2 = "FIRST_OCTET_BINARY"
string3 = "FIRST_OCTET_HEX"

# lifted from Kyle
if len(ipNetAddyList) == 3:
    ipNetAddyList.append('0')
elif len(ipNetAddyList) == 4:
    ipNetAddyList[3] = '0'

# print ipNetAddyList

fullNetAddy = "%s.%s.%s.%s" % (ipNetAddyList[0],ipNetAddyList[1],ipNetAddyList[2],ipNetAddyList[3])
firstOctetBin = bin(int(ipNetAddyList[0]))
firstOctetHex = hex(int(ipNetAddyList[0]))
print
print "IP Network: %s" % fullNetAddy
print
print "%-20s %-20s %-20s" % (string1, string2, string3)
print "%-20s %-20s %-20s" % (fullNetAddy, firstOctetBin, firstOctetHex)
print
