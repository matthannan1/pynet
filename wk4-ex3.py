import pprint
print



uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'


uptimeDict1 = {}
uptimeDict2 = {}

# A fancy use of For loop that I stole from Kirk.
# I was not sure how to loop through each of the four strings,
# and this solves it nicely. Great tip.
for i in (uptime1, uptime2, uptime3, uptime4):
    # Eureka! moment
    # Further refined to doing it all in one go, rather than creating
    # List in values from Dict1 and storing in Dict2
    uptimeDict1[i.split(' uptime is ')[0]] \
    = i.split(' uptime is ')[1].split(', ')

#print uptimeDict1.keys()
#print uptimeDict1.values()
#print
#pprint.pprint(uptimeDict1.viewitems())
#print

# Very cool way to iterate through a dictionary.
# This takes the same keys (aka hostnames) into second dictionary.
# Also allows splitting of uptime info.
#for key, value in uptimeDict1.iteritems():
#    time = 0

#    for i in value:
#        if 'minutes' in value[int(i)]:
#            secMin = 60 * int(i.split()[0]) # seconds in minutes
#            print "Seconds in Minutes = %d" % secMin

#            secHour = int(i.split()[0] * 3600) # seconds in hour
#            print "Seconds in Hours = %d" % secHour



print
print "Dict1:"
pprint.pprint(uptimeDict1)
print
print "Dict2"
pprint.pprint(uptimeDict2)
