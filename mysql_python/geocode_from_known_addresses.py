import csv
import sys

def geocode(filename1,filename2):
    with open(filename1, 'rb') as input_file, open(filename2, 'rb') as ref_file:

        ref = csv.reader(ref_file)
        header = ref.next()
        iaddress = header.index('Address')
        izip = header.index('Zip Code')

        ilat = header.index('Lat')
        ilon = header.index('Lon')

        address = []  # Initialize address / zip tuples
        coord = []  # Initialize lat / lon tuples 

        for row in ref:
            address.append((row[iaddress], row[izip]))
            coord.append((row[ilat], row[ilon]))

        info = csv.reader(input_file)
        header = info.next()
        iaddress = header.index('Address')
        izip = header.index('Zip_Code')

        newrows = []  # Initialize clean rows
        for i, row in enumerate(info):
            if (row[iaddress], row[izip]) in address:
                index = address.index((row[iaddress], row[izip]))
                row.append(coord[index][0])
                row.append(coord[index][1])
                newrows.append(row)
            else:
                row.append(None)
                row.append(None)
                newrows.append(row)
            
    nname = filename1[:-4] + "_geocoded.csv" # The filename of the output file
    header.append('Lat')
    header.append('Lon')
    with open(nname, "wb") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        writer.writerows(newrows)
    return nname

def main():
    #First file geocode based on second file as reference
    fname1 = sys.argv[1]
    fname2 = sys.argv[2]
    nname = geocode(fname1,fname2)
    return nname
    
if __name__ == '__main__':
    main()