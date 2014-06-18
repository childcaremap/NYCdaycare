import time
time.clock()
import sys

from combine_same_address import combine_same
from combine_geocode import combine_geocode
from combine_same_geolocation import combine_samegeo

def main():
    fname = sys.argv[1]
    fname2 = combine_same(fname)
    print fname2
    fname3 = combine_geocode(fname2)
    print fname3
    fname4 = combine_samegeo(fname3)
    print fname4
    time_elapsed = time.clock()
    print [str(time_elapsed)+" seconds"]
    print [str(time_elapsed/60)+" minutes"]

if __name__ == '__main__':
    main()