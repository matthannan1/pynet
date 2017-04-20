# My version

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"
list = cisco_ios.split(", ")
list2 = list[2].split()
ios_ver = list2[1]
print "ios_version = %s" % ios_ver
print

# Kyle's Version

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), \
Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"
ios_version = cisco_ios.split(",")[2]
ios_version = ios_version.split("Version ")[1]
print ios_version
print

# Carving up Kyle's version to see how it works

print cisco_ios.split(",")
print
ios_version1 = cisco_ios.split(",")[2]
print cisco_ios.split(",")[0]
print cisco_ios.split(",")[1]
print cisco_ios.split(",")[2]
print cisco_ios.split(",")[3]
print "------------"
print "A: " +ios_version1
print "B: " + str(ios_version1.split("Version "))
print "C: " +ios_version1.split("Version ")[0]
print "D: " +ios_version1.split("Version ")[1]
ios_version2 = ios_version1.split("Version ")[1]
print "------------"
print "ios_version1.split('Version ')[1] : %s" % ios_version2
print
