import urllib2
import re

path = 'https://raw.githubusercontent.com/ktbyers/pynet/master/learnpy_ecourse/class7/CDP_DATA/r1_cdp.txt'
a_file = urllib2.urlopen(path)

# Make the file contents a string.
# This is so that you can easily search it
# using Regular Expressions
cdp_data = a_file.read()
# This might not be needed, but can't hurt.
a_file.close()

#print cdp_data

remote_hostname = re.search(r"Device ID: (.+)", cdp_data)
remote_IP = re.search(r"IP address: (.+)", cdp_data)
remote_platform = re.search(r"Platform: (.+?) (.+?), ", cdp_data)
remote_model = remote_platform.group(2)
remote_vendor = remote_platform.group(1)
remote_device_type = re.search(r"Capabilities: (.+)", cdp_data)



print "Hostname: %s" % remote_hostname.group(1)
print "IP Address: %s" % remote_IP.group(1)
print "Vendor: %s" % remote_vendor
print "Model: %s" % remote_model
print "Device Type: %s" % remote_device_type.group(1)



