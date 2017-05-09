import pprint
print

# The output to parse through
sh_ver = """
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)
twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X
5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X
License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices
Configuration register is 0x2102
"""

# Split the output by line into a List
sh_ver_List = sh_ver.split("\n")

# Create a Dictionary
sh_ver_Dict = {}

#print type(sh_ver_List)
#print sh_ver_List
#print sh_ver_Dict

# run through each line looking for vendor, model, os_version, uptime, and serial_number

for line in sh_ver_List:

    if 'Cisco IOS Software' in line:
        sh_ver_Dict['vendor'] = 'Cisco'
        # This is cool. Split line by csv, then take third string
        os_version = line.split(',')[2]
        # Then split this by Version and take second string and write it to dictionary
        sh_ver_Dict['os_version'] = os_version.split('Version ')[1]

    if 'processor' in line:
        model = line.split()[1]
        sh_ver_Dict['model'] = model
        # Can actually assign split string directly to dictionary sans variable
        # sh_ver_Dict['model'] = line.split()[1]

    if 'uptime' in line:
        sh_ver_Dict['uptime'] = line.split('is ')[1]

    if 'Processor board ID' in line:
        sh_ver_Dict['serial_number'] = line.split('Processor board ID ')[1]


print sh_ver_Dict
print
print "And a little nicer, using pprint..."
print
pprint.pprint(sh_ver_Dict)


		