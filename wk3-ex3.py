import pprint


shipintbr = ["FastEthernet0   unassigned      YES     unset          up          up",
             "FastEthernet1   unassigned      YES     unset          up          up",
             "FastEthernet2   unassigned      YES     unset          down      down",
             "FastEthernet3   unassigned      YES     unset          up          up",
             "FastEthernet4    6.9.4.10          YES     NVRAM       up          up",
             "NVI0                  6.9.4.10          YES     unset           up          up",
             "Tunnel1            16.25.253.2     YES     NVRAM       up          down",
             "Tunnel2            16.25.253.6     YES     NVRAM       up          down",
             "Vlan1                unassigned      YES    NVRAM       down      down",
             "Vlan10              10.220.88.1     YES     NVRAM       up          up",
             "Vlan20              192.168.0.1     YES     NVRAM       down      down",
             "Vlan100            10.220.84.1     YES     NVRAM       up          up"]

cleanedUp = []

for i in shipintbr:
    element = i.split()
    if element[4] == 'up' and element[5] == 'up':
        tup = (element[0],element[1],element[4],element[5])
        cleanedUp.append(tup)

#print cleanedUp
# Haven't told you about this, but this just prints the list out nicer
pprint.pprint(cleanedUp)
print "\n"
