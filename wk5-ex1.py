##### Python Shell - experimenting with dictionary of dictionaries #####

# Initialize network_devices to be a blank dictionary
# >>> network_devices = {}

# Assign the key 'R1' to network_devices using a value of a blank dictionary (in other words, I am adding a key:value pair to network_devices where the key is 'R1' and the value is {} )
# >>> network_devices['R1'] = {}

# Look at network_devices at this point
# >>> network_devices
#   {'R1': {}}

# Add the 'ip' and 'vendor' fields to the inner dictionary
# >>> network_devices['R1']['ip'] = '10.1.1.1'
# >>> network_devices['R1']['vendor'] = 'Cisco'
# >>> network_devices
#   {'R1': {'ip': '10.1.1.1', 'vendor': 'Cisco'}}

##### Python Shell - experimenting end #####

##### Start of the cdp info - might be better as external file

sw1_show_cdp_neighbors = '''
SW1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone
Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R1           Fas 0/11        153           R S I           881          Fas 1
R2           Fas 0/12        123           R S I           881          Fas 1
R3           Fas 0/13        129           R S I           881          Fas 1
R4           Fas 0/14        173           R S I           881          Fas 1
R5           Fas 0/15        144           R S I           881          Fas 1
'''

sw1_show_cdp_neighbors_detail = '''
SW1> show cdp neighbors detail
--------------------------
Device ID: R1
Entry address(es):
   IP address: 10.1.1.1
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/11, Port ID (outgoing port): FastEthernet1
Holdtime: 153 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R2
Entry address(es):
   IP address: 10.1.1.2
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/12, Port ID (outgoing port): FastEthernet1
Holdtime: 123 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R3
Entry address(es):
   IP address: 10.1.1.3
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/13, Port ID (outgoing port): FastEthernet1
Holdtime: 129 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R4
Entry address(es):
   IP address: 10.1.1.4
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/14, Port ID (outgoing port): FastEthernet1
Holdtime: 173 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R5
Entry address(es):
   IP address: 10.1.1.5
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/15, Port ID (outgoing port): FastEthernet1
Holdtime: 144 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
'''

r1_show_cdp_neighbors = '''
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/11
'''

r1_show_cdp_neighbors_detail = '''
R1>show cdp neighbors detail
-------------------------
Device ID: SW1
Entry address(es):
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/11
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r2_show_cdp_neighbors = '''
R2>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/12
'''

r2_show_cdp_neighbors_detail = '''
R2>show cdp neighbors detail
-------------------------
Device ID: SW1
Entry address(es):
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/12
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r3_show_cdp_neighbors = '''
R3>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/13
'''

r3_show_cdp_neighbors_detail = '''
R3>show cdp neighbors detail
-------------------------
Device ID: SW1
Entry address(es):
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/13
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r4_show_cdp_neighbors = '''
R4>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/14
'''

r4_show_cdp_neighbors_detail = '''
R4>show cdp neighbors detail
-------------------------
Device ID: SW1
Entry address(es):
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/14
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r5_show_cdp_neighbors = '''
R5>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/15
'''

r5_show_cdp_neighbors_detail = '''
R5>show cdp neighbors detail
-------------------------
Device ID: SW1
Entry address(es):
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/15
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''
##### End of cdp details #####

##### Start of script #####
import pprint
# Gather all of that into a tuple (could be list, too)
bundled_cdp_details = (
    sw1_show_cdp_neighbors_detail,
    r1_show_cdp_neighbors_detail,
    r2_show_cdp_neighbors_detail,
    r3_show_cdp_neighbors_detail,
    r4_show_cdp_neighbors_detail,
    r5_show_cdp_neighbors_detail,
)

# Create dictionary
network_devices = {}

for cdp_data in bundled_cdp_details:
    cdp_data_line = cdp_data.split("\n")
#    print cdp_data_line
#    print

    # Reset hostname for each cdp output
    hostname = ''

    # Iterate over each line of the cdp data
    for line in cdp_data_line:

        # As a precaution set hostname to '' on every device divider
        if '----------------' in line:
            hostname = ''

        # Processing hostname
        if 'Device ID: ' in line:
            (junk, hostname) = line.split('Device ID: ')
            hostname = hostname.strip()

            if not hostname in network_devices:
                network_devices[hostname] = {}

#        print hostname

        # Processing IP
        if 'IP address: ' in line:
            (junk, ip) = line.split('IP address: ')
            ip = ip.strip()
#            print junk
            if hostname:
                network_devices[hostname]['ip'] = ip

        # Process vendor, model, and device_type
        if 'Platform: ' in line:

            (platform, capabilities) = line.split(',')

            # Process vendor and model
            (junk, model_vendor) = platform.split("Platform: ")
            (vendor, model) = model_vendor.split()

            # Process device_type
            (junk, capabilities) = capabilities.split("Capabilities: ")
            if 'Router' in capabilities:
                device_type = 'router'
            elif 'Switch' in capabilities:
                device_type = 'switch'
            else:
                device_type = 'unknown'

            if hostname:
                network_devices[hostname]['vendor'] = vendor
                network_devices[hostname]['model'] = model
                network_devices[hostname]['device_type'] = device_type


print '\n'
pprint.pprint(network_devices)
print '\n'
