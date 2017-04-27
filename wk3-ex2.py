str1 = "IP_Prefix"
str2 = "AS_Path"

entry = ["*  1.0.192.0/18   157.130.10.233     0 701 38040 9737 i",
         "*  1.1.1.0/24       157.130.10.233     0 701 1299 15169 i",
         "*  1.1.42.0/24     157.130.10.233     0 701 9505 17408 2.1465 i",
         "*  1.0.192.0/19   157.130.10.233     0 701 6762 6762 6762 6762 38040 9737 i"]

print
print "%-16s %-16s" % (str1, str2)

for i in entry:
#    print "DEBUG 1: ", i
    list = i.split()
#    print "DEBUG 2: ", list
    ipPrefix = list[1]
#    print "DEBUG 3: ", ipPrefix
    asPath = list[4:-1]
#    print "DEBUG 4: ", asPath
    print "%-16s %-16s" % (ipPrefix,asPath)

print
