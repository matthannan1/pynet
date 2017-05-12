print

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

# Create dictionary from strings.
uptimeDict = {}

# A fancy use of For loop that I stole from Kirk.
# I was not sure how to loop through each of the four strings,
# and this solves it nicely. Great tip.
for i in (uptime1, uptime2, uptime3, uptime4):
    # Eureka! moment
    # Further refined to doing it all in one go, rather than creating
    # List in values from Dict1 and storing in Dict2
    uptimeDict[i.split(' uptime is ')[0]] \
    = i.split(' uptime is ')[1].split(', ')

# Very cool way to iterate through a dictionary.
# This takes the same keys (aka hostnames) into second dictionary.
# Also allows splitting of uptime info.
for key, value in uptimeDict.items():
    # zero out everything on each pass through the dictionary entries
    seconds = 0
    secMins = 0
    secHours = 0
    secDays = 0
    secWeeks = 0
    secYears = 0

    for time_unit in value:

        if 'minute' in time_unit:
            minutes = int(time_unit.split()[0])
            secMins = minutes * 60

        if 'hour' in time_unit:
            hours = int(time_unit.split()[0])
            secHours = hours * 3600

        if 'day' in time_unit:
            days = int(time_unit.split()[0])
            secDays = days * 86400

        if 'week' in time_unit:
            weeks = int(time_unit.split()[0])
            secWeeks = weeks * 604800

        if 'year' in time_unit:
            years = int(time_unit.split()[0])
            secYears = years * (604800*52)

        seconds = secMins + secHours + secDays + secWeeks + secYears
    print "%-12s:%15d seconds of uptime" % (key, seconds)
