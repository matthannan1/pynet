import urllib2
import re

path = 'https://raw.githubusercontent.com/ktbyers/pynet/master/learnpy_ecourse/class7/CDP_DATA/sw1_cdp.txt'
a_file = urllib2.urlopen(path)

# Make the file contents a string.
# This is so that you can easily search it
# using Regular Expressions
cdp_data = a_file.read()
# This might not be needed, but can't hurt.
a_file.close()

#print cdp_data

remote_hosts = re.findall(r"Device ID: (.+)", cdp_data)
remote_IPs = re.findall(r"IP address: (.+)", cdp_data)
remote_platform = re.findall(r"Platform: (.+?), ", cdp_data)


print remote_hosts
print remote_IPs
print remote_platform




