import sys
import csv

def combine_samegeo(filename):
    with open(filename, 'rb') as input_file:
        info = csv.reader(input_file)
        header = info.next()
        iname = header.index('Center Name')
        iholder = header.index('Permit Holder')
        iaddress = header.index('Address')
        izip= header.index('Zip Code')
        iphone = header.index('Phone')
        ipermit = header.index('Permit Number')
        iexp = header.index('Permit Expiration Date')
        istatus = header.index('Permit Status')
        iagerange= header.index('Age Range')
        icap = header.index('Maximum Capacity')
        imed = header.index('Certified to Administer Medication')
        itype = header.index('Site Type')
        ilat = header.index('Lat')
        ilon = header.index('Lon')
        itotcap = header.index('Total Maximum Capacity')

        newrows = []  # Initialize clean rows
        coord = []  # Initialize coordinate tupels
        # add entry only if geolocation hasn't been added yet
        for row in info:
            if (row[ilat], row[ilon]) not in coord:
                coord.append((row[ilat], row[ilon]))
                newrows.append(row)
            else:
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
                combstatus = row[istatus] + ' / ' + newrows[i_comb][istatus]
                newrows[i_comb][istatus] = combstatus
                combagerange = row[iagerange] + ' / ' + newrows[i_comb][iagerange]
                newrows[i_comb][iagerange] = combagerange
                combcap = row[icap] + ' / ' + newrows[i_comb][icap]
                newrows[i_comb][icap] = combcap
                combmed = row[imed] + ' / ' + newrows[i_comb][imed]
                newrows[i_comb][imed] = combmed
                combtype = row[itype] + ' / ' + newrows[i_comb][itype]
                newrows[i_comb][itype] = combtype
                newrows[i_comb][itotcap] = int(newrows[i_comb][itotcap]) + int(row[itotcap])

    nname = filename[:-4] + "_combinedgeo.csv" # The filename of the output file

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