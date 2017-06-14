import urllib2
import re

path = 'https://raw.githubusercontent.com/ktbyers/pynet/master/learnpy_ecourse/class7/OSPF_DATA/ospf_single_interface.txt'
a_file = urllib2.urlopen(path)

# Make the file contents a string.
# This is so that you can easily search it
# using Regular Expressions
ospf_data = a_file.read()
# This might not be needed, but can't hurt.
a_file.close()

ospf_dict = {}

interface = re.search(r"^(.+) is up, line protocol is up", ospf_data)
ip_addr = re.search(r"Internet Address (.+?),", ospf_data)
area = re.search(r"Area (.+?), ", ospf_data)
type = re.search(r"Network Type (.+?), Cost: (.+)", ospf_data)
hello = re.search(r"Hello (.+?),", ospf_data)
dead = re.search(r"Dead (.+?),", ospf_data)


ospf_dict["Int"] = interface.group(1)
ospf_dict["IP"] = ip_addr.group(1)
ospf_dict["Area"] = area.group(1)
ospf_dict["Type"] = type.group(1)
ospf_dict["Cost"] = type.group(2)
ospf_dict["Hello"] = hello.group(1)
ospf_dict["Dead"] = dead.group(1)

# Fancy Kirk stuff
print
field_order = ('Int', 'IP', 'Area', 'Type', 'Cost', 'Hello', 'Dead')
for k in field_order:
    print "%10s: %-20s" % (k, ospf_dict[k])
print







