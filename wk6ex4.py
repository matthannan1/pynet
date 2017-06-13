# convert IP to binary

def ip2binary(ip_address):
    # Master Control
    if len(input) != 2:
        sys.exit("Invalid input. Run program again with proper data.")

    # Pull IP from argv
    ip_addr = input[1]

    # Convert IP string to ipList
    ipList = ip_addr.split('.')

    # Verify IP Address Length
    if len(ipList) != 4:
        sys.exit("Invalid IP address.")

    # convert octets to Binary
    binList = []
    for i in ipList:
        binOct = bin(int(i))
        # strip off the 0b, or first two, characters
        binOct = binOct[2:]
        # padding to 8 characters
        while len(binOct) <= 8:
            binOct = '0' + binOct
            # add binOct to list
        binList.append(binOct)

    # combine binList elements to binAddy string
    binAddy = ".".join(binList)
    return binAddy

def padded_print(ip_address,binary_address):
    padded = "%-20s %-20s" % (ip_address, binary_address)
    return padded
