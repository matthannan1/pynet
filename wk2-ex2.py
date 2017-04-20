print
ipAddy = raw_input("Enter an IP address: ")

str1 = "First_Octet"
str2 = "Second_Octet"
str3 = "Third_Octet"
str4 = "Fourth_Octet"

ipAddyList = ipAddy.split(".")
oct1 = bin(int(ipAddyList[0]))
oct2 = bin(int(ipAddyList[1]))
oct3 = bin(int(ipAddyList[2]))
oct4 = bin(int(ipAddyList[3]))

print
print "%-15s %-15s %-15s %-15s" % (str1, str2, str3, str4)
print "%-15s %-15s %-15s %-15s" % (oct1, oct2, oct3, oct4)
print

 
