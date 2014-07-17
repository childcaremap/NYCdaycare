import sys
import csv

def combine_samegeo(filename):
    with open(filename, 'rb') as input_file:
        info = csv.reader(input_file)
        header = info.next()
        iid = header.index('Site_ID')
        iname = header.index('Center_Name')
        iholder = header.index('Permit_Holder')
        iaddress = header.index('Address')
        izip= header.index('Zip_Code')
        iphone = header.index('Phone')
        ipermit = header.index('Permit_Number')
        iexp = header.index('Permit_Expiration_Date')
        istatus = header.index('Permit_Status')
        iagerange= header.index('Age_Range')
        icap = header.index('Maximum_Capacity')
        imed = header.index('Certified_to_Administer_Medication')
        itype = header.index('Site_Type')
        invio = header.index('Number_Of_Violations')
        inhaz = header.index('Hazard_Violations')
        incri = header.index('Critical_Violations')
        ingen = header.index('General_Violations')
        invis = header.index('Number_Of_Visits')
        #imedvio = header.index('Median_Violations_Per_Visit')
        imeavio = header.index('Mean_Violations_Per_Visit')
        #imedran = header.index('Median_Rank')
        imearan = header.index('Mean_Rank')
        #imedcat = header.index('Median_Cat')
        imeacat = header.index('Mean_Cat')
        inpermits = header.index('Number_Of_Permits')
        iavmeavio = header.index('Average_Mean_Violations_Per_Visit')
        ilat = header.index('Lat')
        ilon = header.index('Lon')

        newrows = []  # Initialize clean rows
        coord = []  # Initialize coordinate tupels
        # add entry only if geolocation hasn't been added yet
        for row in info:
            if (row[ilat], row[ilon]) not in coord:
                coord.append((row[ilat], row[ilon]))
                newrows.append(row)
            else:
                i_comb = coord.index((row[ilat], row[ilon]))
                combid = row[iid] + ' / ' + newrows[i_comb][iid]
                newrows[i_comb][iid] = combid
                combname = row[iname] + ' / ' + newrows[i_comb][iname]
                newrows[i_comb][iname] = combname
                combholder = row[iholder] + ' / ' + newrows[i_comb][iholder]
                newrows[i_comb][iholder] = combholder
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
                combnvio = row[invio] + ' / ' + newrows[i_comb][invio]
                newrows[i_comb][invio] = combnvio
                combnhaz = row[inhaz] + ' / ' + newrows[i_comb][inhaz]
                newrows[i_comb][inhaz] = combnhaz
                combncri = row[incri] + ' / ' + newrows[i_comb][incri]
                newrows[i_comb][incri] = combncri
                combngen = row[ingen] + ' / ' + newrows[i_comb][ingen]
                newrows[i_comb][ingen] = combngen
                combnvis = row[invis] + ' / ' + newrows[i_comb][invis]
                newrows[i_comb][invis] = combnvis
                #combmedvio = row[imedvio] + ' / ' + newrows[i_comb][imedvio]
                #newrows[i_comb][imedvio] = combmedvio
                combmeavio = row[imeavio] + ' / ' + newrows[i_comb][imeavio]
                newrows[i_comb][imeavio] = combmeavio
                #combmedran = row[imedran] + ' / ' + newrows[i_comb][imedran]
                #newrows[i_comb][imedran] = combmedran
                combmearan = row[imearan] + ' / ' + newrows[i_comb][imearan]
                newrows[i_comb][imearan] = combmearan
                #combmedcat = row[imedcat] + ' / ' + newrows[i_comb][imedcat]
                #newrows[i_comb][imedcat] = combmedcat
                combmeacat = row[imeacat] + ' / ' + newrows[i_comb][imeacat]
                newrows[i_comb][imeacat] = combmeacat

                if row[imeavio] != '':
                    if newrows[i_comb][iavmeavio] != '':
                        newrows[i_comb][iavmeavio] = (int(row[inpermits])*float(row[iavmeavio]) + int(newrows[i_comb][inpermits])*float(newrows[i_comb][iavmeavio]))/(int(row[inpermits]) + int(newrows[i_comb][inpermits]))
                        newrows[i_comb][inpermits] = int(row[inpermits]) + int(newrows[i_comb][inpermits])
                    else:
                        newrows[i_comb][iavmeavio] = float(row[imeavio])
                        newrows[i_comb][inpermits] = int(newrows[i_comb][inpermits]) + 1

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