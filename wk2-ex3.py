entry1 = "*  1.0.192.0/18   157.130.10.233     0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233     0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233     0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233     0 701 6762 6762 6762 6762 38040 9737 i"

list1 = entry1.split()
list2 = entry2.split()
list3 = entry3.split()
list4 = entry4.split()

str1 = "IP_Prefix"
str2 = "AS_Path"

ipPrefix1 = list1[1]
asPath1 = list1[4:-1]
ipPrefix2 = list2[1]
asPath2 = list2[4:-1]
ipPrefix3 = list3[1]
asPath3 = list3[4:-1]
ipPrefix4 = list4[1]
asPath4 = list4[4:-1]

print
print "%-16s %-16s" % (str1, str2)
print "%-16s %-16s" % (ipPrefix1,asPath1)
print "%-16s %-16s" % (ipPrefix2,asPath2)
print "%-16s %-16s" % (ipPrefix3,asPath3)
print "%-16s %-16s" % (ipPrefix4,asPath4)
print
