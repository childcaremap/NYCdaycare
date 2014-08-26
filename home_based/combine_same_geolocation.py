import sys
import csv
import re

def combine_samegeo(filename):
    with open(filename, 'rb') as input_file:
        info = csv.reader(input_file)
        header = info.next()
        iaddress = 15
        header.insert(iaddress,'Address')

        iname = header.index('Facility Name')
        iholder = header.index('Provider Name')

        inumber = header.index('Street Number')
        istreet = header.index('Street Name')
        iadd = header.index('Additional Address')
        ifloor = header.index('Floor')
        iapt = header.index('Apartment')
        
        izip= header.index('Zip Code')
        iborough = header.index('County')

        iphone = header.index('Phone Number')
        ipermit = header.index('Facility ID')
        iexp = header.index('License Expiration Date')
        iopen = header.index('Facility Opened Date')
        iissue = header.index('License Issue Date')
        istatus = header.index('Facility Status')
        icap = header.index('Capacity Description')
        iinfo = header.index('Additional Information')
        itype = header.index('Program Type')

        ilat = header.index('Latitude')
        ilon = header.index('Longitude')

        newrows = []  # Initialize clean rows
        coord = []  # Initialize coordinate tupels
        # add entry only if geolocation hasn't been added yet
        for row in info:
            address = row[inumber] + ' ' + row[istreet]
            if row[iadd] != '':
                address = address + ', ' + row[iadd]
            if row[ifloor] != '':
                address = address + ', Floor ' + row[ifloor]
            if row[iapt] != '':
                address = address + ', Apt. ' + row[iapt]
            row.insert(iaddress,address)

            row[icap] = re.sub(' Children','',row[icap])
            row[icap] = re.sub('Ages ','',row[icap])
            link = re.sub(re.escape('viewprofile.aspx?&facility_id='),'Profile/Index/',row[iinfo])
            row[iinfo] = '<a href="' + link + '" target="_blank">' + link + '</a>'
            if (row[ilat], row[ilon]) not in coord:
                if row[ilat] != '':
                    coord.append((row[ilat], row[ilon]))
                    newrows.append(row)
            else:
                if row[ilat] != '':
                    #coord.append((row[ilat], row[ilon]))
                    #newrows.append(row)
                #else:
                    i_comb = coord.index((row[ilat], row[ilon]))
                    combname = row[iname] + ' / ' + newrows[i_comb][iname]
                    newrows[i_comb][iname] = combname
                    combholder = row[iholder] + ' / ' + newrows[i_comb][iholder]
                    newrows[i_comb][iholder] = combholder
                    combaddress = row[iaddress] + ' / ' + newrows[i_comb][iaddress]
                    newrows[i_comb][iaddress] = combaddress
                    combphone = row[iphone] + ' / ' + newrows[i_comb][iphone]
                    newrows[i_comb][iphone] = combphone
                    combpermit = row[ipermit] + ' / ' + newrows[i_comb][ipermit]
                    newrows[i_comb][ipermit] = combpermit
                    combexp = row[iexp] + ' / ' + newrows[i_comb][iexp]
                    newrows[i_comb][iexp] = combexp
                    combopen = row[iopen] + ' / ' + newrows[i_comb][iopen]
                    newrows[i_comb][iopen] = combopen
                    combissue = row[iissue] + ' / ' + newrows[i_comb][iissue]
                    newrows[i_comb][iissue] = combissue
                    combstatus = row[istatus] + ' / ' + newrows[i_comb][istatus]
                    newrows[i_comb][istatus] = combstatus
                    combinfo = row[iinfo] + ' / ' + newrows[i_comb][iinfo]
                    newrows[i_comb][iinfo] = combinfo
                    combcap = row[icap] + ' / ' + newrows[i_comb][icap]
                    newrows[i_comb][icap] = combcap
                    combtype = row[itype] + ' / ' + newrows[i_comb][itype]
                    newrows[i_comb][itype] = combtype

    nname = filename[:-4] + "_combinedgeo.csv" # The filename of the output file
    for newrow in newrows:
        #remove unuseful information
        newrow.pop(33)
        newrow[25:30] = []
        #remove individual address components
        newrow[10:15] = []

    with open(nname, "wb") as output_file:
        writer = csv.writer(output_file)
        header.pop(33)
        header[25:30] = []
        header[10:15] = []
        writer.writerow(header)
        writer.writerows(newrows)
    return nname

def main():
    fname = sys.argv[1]
    nname = combine_samegeo(fname)
    return nname
    
if __name__ == '__main__':
    main()