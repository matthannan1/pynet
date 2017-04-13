# Split an IPv6 address into 4 hex numbers

ipv6Address = "FE80:0000:0000:0000:0101:A3EF:EE1E:1719"
print "\nIPv6 address: ", ipv6Address
octets = ipv6Address.split(':')

print "All split up:"
print(octets)

# Rejoin the octets and assign tio a new variable name

rejoinedAddress = ":".join(octets)
print "Rejoined address is: ", rejoinedAddress 
