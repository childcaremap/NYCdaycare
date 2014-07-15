import sys
import csv
from pygeocoder import Geocoder

def combine_samegeo(filename):
    with open(filename, 'rb') as input_file:
        info = csv.reader(input_file)
        header = info.next()

        inumber = header.index('Street Number')
        istreet = header.index('Street Name')
        iadd = header.index('Additional Address')
        ifloor = header.index('Floor')
        iapt = header.index('Apartment')
        
        izip= header.index('Zip Code')
        iborough = header.index('County')

        ilat = header.index('Latitude')
        ilon = header.index('Longitude')

        newrows = []  # Initialize clean rows
        # add entry only if geolocation hasn't been added yet
        for row in info:
            if row[ilat] == '0':
                if row[iborough] == 'MANHATTAN':
                    geoaddress =  row[inumber] + ' ' + row[istreet] +', NEW YORK, NY ' + row[izip]
                else:
                    geoaddress = row[inumber] + ' ' + row[istreet] + ', ' + row[iborough] + ', NY ' + row[izip]
                try:
                    result = Geocoder.geocode(geoaddress)
                    if len(result) == 1:
                        row[ilat] = result.coordinates[0]
                        row[ilon] = result.coordinates[1]
                    else:
                        row[ilat] = result[0].coordinates[0]
                        row[ilon] = result[0].coordinates[1]
                        print 'more than one geolocation found for ' + geoaddress
                except:
                    print 'geocoding failed'
            newrows.append(row)


    nname = filename[:-4] + "_geocoded.csv" # The filename of the output file
    with open(nname, "wb") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        writer.writerows(newrows)
    return nname

def main():
    fname = sys.argv[1]
    nname = combine_samegeo(fname)
    return nname
    
if __name__ == '__main__':
    main()