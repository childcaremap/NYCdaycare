import sys
import csv

def combine_samegeo(filename):
    with open(filename, 'rb') as input_file:
        info = csv.reader(input_file)
        header = info.next()
        iID = header.index('Site ID')
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
        imed = header.index('Certified To Administer Medication')
        itype = header.index('Site Type')
        ilat = header.index('Lat')
        ilon = header.index('Lon')
        isumm = header.index('Summary')
        idate = header.index('Last Visit Date')
        ivisit = header.index('Visit Type')


        newrows = []  # Initialize clean rows
        coord = []  # Initialize coordinate tupels
        # add entry only if geolocation hasn't been added yet
        for row in info:
            if (row[ilat], row[ilon]) not in coord:
                coord.append((row[ilat], row[ilon]))
                newrows.append(row)
                #add column for total capacity at same geolocation
                ind = len(newrows)-1
                newrows[ind].append(int(row[icap]))
            else:
                i_comb = coord.index((row[ilat], row[ilon]))
                combID = row[iID] + ' / ' + newrows[i_comb][iID]
                newrows[i_comb][iID] = combID
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
                combsumm = row[isumm] + ' / ' + newrows[i_comb][isumm]
                newrows[i_comb][isumm] = combsumm
                combdate = row[idate] + ' / ' + newrows[i_comb][idate]
                newrows[i_comb][idate] = combdate
                combvisit = row[ivisit] + ' / ' + newrows[i_comb][ivisit]
                newrows[i_comb][ivisit] = combvisit
                #add up total capacity at same geolocation
                newrows[i_comb][-1] = newrows[i_comb][-1] + int(row[icap])

    nname = filename[:-4] + "_combinedgeo.csv" # The filename of the output file
    header.append('Total Maximum Capacity')
    with open(nname, "wb") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        writer.writerows(newrows)

def main():
    fname = sys.argv[1]
    combine_samegeo(fname)

if __name__ == '__main__':
    main()