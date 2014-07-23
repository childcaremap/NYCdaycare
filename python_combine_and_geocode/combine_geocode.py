import csv
import time
import sys
from pygeocoder import Geocoder

def combine_geocode(filename):
    with open(filename, 'rb') as input_file:
        info = csv.reader(input_file)
        header = info.next()
        iaddress = header.index('Address')
        iborough = header.index('Borough')
        izip= header.index('Zip Code')
        
        k = 0
        newrows = []  # Initialize clean rows
        # retrieve geolocation from Google API
        for i, row in enumerate(info):
            print i
            if row[iborough] == 'MANHATTAN':
                address =  row[iaddress] +', NEW YORK, NY ' + row[izip]
            else:
                address = row[iaddress] +', ' + row[iborough] + ', NY ' + row[izip]
            try:
                result = Geocoder.geocode(address)
                time.sleep(.5)
                if len(result) == 1:
                    row.append(result.coordinates[0])
                    row.append(result.coordinates[1])
                    newrows.append(row)
                else:
                    print 'more than one geolocation found for ' + address
                    row.append(result[0].coordinates[0])
                    row.append(result[0].coordinates[1])
                    newrows.append(row)
            except:
                k = k + 1
                row.append(None)
                row.append(None)
                newrows.append(row)
                continue
            
    print str(k) + ' entries not geocoded'

    nname = filename[:-4] + "_geocoded.csv" # The filename of the output file
    header.append('Lat')
    header.append('Lon')
    with open(nname, "wb") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        writer.writerows(newrows)
    return nname

def main():
    fname = sys.argv[1]
    nname = combine_geocode(fname)
    return nname
    
if __name__ == '__main__':
    main()