import sys
import wk6ex3a
import wk6ex4
print

input = raw_input('Enter an IP address: ')

if wk6ex3a.IPvalidator(input):
    string1 = "IP Address"
    string2 = "Binary"
#    print input
    print "%-20s %-20s" % (string1, string2)
    print "%-20s %-20s" % (input, wk6ex4.ip2binary(input))
else:
    print "Bad IP, yo"
