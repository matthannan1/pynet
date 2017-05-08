# IP address validator with Try-Exception

import sys
print

notDone = True

while notDone:

    input = raw_input('Enter an IP address: ')
    ipList = input.split('.')
    validIP = True
# Does input have four sections?
    if len(ipList) != 4:
        print "Invalid input. Incorrect number of octets. Err 1"
        validIP = False

# Are the four sections integers?
#    print list(enumerate(ipList))
#    octets = []
    for i, octet in enumerate(ipList):
        try:
            ipList[i] = int(octet)
            #print ipList[i]
        except TypeError:
            print "Invalid input. %d is not an integer. Err 2" % ipList[i]
            validIP = False
        except ValueError:
            print "Invalid input. %s is not an integer. Err 2" % octet
            validIP = False

# First octet must be 223 or less
    try:
        if int(ipList[0]) <= 1 or int(ipList[0]) >= 223:
            print "Invalid input. %d is not a valid octet. Err 3" % ipList[0]
            validIP = False
    except ValueError:
        print "Invalid input. %s is not a valid octet. Err 3" % ipList[0]
        validIP = False



# First octet cannot be 127
    try:
        if int(ipList[0]) == 127:
            print "Invalid input. IP address can not be in 127.0.0.0 subnet. Err 4"
            validIP = False
    except ValueError:
        print "Invalid input. %s is not an integer. Err 4" % ipList[0]
        validIP = False

# IP cannot be on the 169.254.0.0 network
    try:
        if int(ipList[0]) == 169 and int(ipList[1]) == 254:
            print "Invalid input. IP address can not be in 169.254.0.0 subnet. Err 5"
            validIP = False
    except ValueError:
        print "Invalid input. %s is not an integer. Err 5" % ipList[1]
        validIP = False

# Are the octets integers between 0 and 255?
    for i in ipList:
        try:
            if int(i) >= 1:
                if int(i) < 0 or int(i) > 255:
                    print "Invalid input. %d is not a valid octet. Err 6" % int(i)
        except ValueError:
            validIP = False

    if validIP:
        notDone = False
print "\nIP Address %s is valid.\n" % input
