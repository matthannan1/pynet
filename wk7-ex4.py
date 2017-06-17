# This code assumes that all of the CDP files are in a subdirectory called
# CDP_DATA beneath the current working directory

#>>> from glob import glob
#>>> cdp_files = glob('CDP_DATA/*_cdp.txt')

#>>> cdp_files
#['CDP_DATA/r1_cdp.txt', 'CDP_DATA/r2_cdp.txt', 'CDP_DATA/r3_cdp.txt',  'CDP_DATA/sw1_cdp.txt', 'CDP_DATA/r4_cdp.txt', 'CDP_DATA/r5_cdp.txt']

from glob import glob
cdp_files = glob('CDP_DATA/*_cdp.txt')

print cdp_files
