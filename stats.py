__author__ = 'charlie'

from collections import defaultdict, Counter
import calendar
import time

# Import this and write to it from protocols (twisted is single threaded remember)
STATS = defaultdict(int)

def topX(stats, x):
    """return top x stats"""
    return Counter(stats).most_common(x)

def topX_json_format(stats, x):
    return [dict([m]) for m in topX(stats, x)]

def topX_graphite_format(stats, x):
    """ return top X in graphite line format (list)"""
    now = calendar.timegm(time.gmtime())
    return [ "{k} {v} {n}".format(k=m[0], v=m[1], n=now) for m in topX(stats, x)]