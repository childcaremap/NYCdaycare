import sys
import csv

def combine_same(filename):
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
	 	iviopervis = len(header)
	 	ihazpervis = len(header)+1
	 	itotcap = len(header)+2
	 	

		newrows = []  # Initialize clean rows
		address = []  # Initialize address / zip tupels
		# add entry only if address hasn't been added yet
		for row in info:
		    if (row[iaddress], row[izip]) not in address:
		        address.append((row[iaddress], row[izip]))
		        newrows.append(row)
		        ind = len(newrows)-1
		        if int(row[invis]) is not 0:
		        	newrows[ind].append("{:.2f}".format(float(row[invio])/float(row[invis])))
		        else:
		        	newrows[ind].append('No Visits')
		        if int(row[invis]) is not 0:
		        	newrows[ind].append("{:.2f}".format(float(row[inhaz])/float(row[invis])))
		        else:
		        	newrows[ind].append('No Visits')
		        newrows[ind].append(int(row[icap]))
		    else:
		    	i_comb = address.index((row[iaddress], row[izip]))
		    	combid = row[iid] + ', ' + newrows[i_comb][iid]
		    	newrows[i_comb][iid] = combid
		    	combname = row[iname] + ', ' + newrows[i_comb][iname]
		    	newrows[i_comb][iname] = combname
		    	combholder = row[iholder] + ', ' + newrows[i_comb][iholder]
		    	newrows[i_comb][iholder] = combholder
		    	combphone = row[iphone] + ', ' + newrows[i_comb][iphone]
		    	newrows[i_comb][iphone] = combphone
		    	combpermit = row[ipermit] + ', ' + newrows[i_comb][ipermit]
		    	newrows[i_comb][ipermit] = combpermit
		    	combexp = row[iexp] + ', ' + newrows[i_comb][iexp]
		    	newrows[i_comb][iexp] = combexp
		    	combstatus = row[istatus] + ', ' + newrows[i_comb][istatus]
		    	newrows[i_comb][istatus] = combstatus
		    	combagerange = row[iagerange] + ', ' + newrows[i_comb][iagerange]
		    	newrows[i_comb][iagerange] = combagerange
		    	combcap = row[icap] + ', ' + newrows[i_comb][icap]
		    	newrows[i_comb][icap] = combcap
		    	combmed = row[imed] + ', ' + newrows[i_comb][imed]
		    	newrows[i_comb][imed] = combmed
		    	combtype = row[itype] + ', ' + newrows[i_comb][itype]
		    	newrows[i_comb][itype] = combtype
		    	# add up for total capacity
		    	newrows[i_comb][itotcap] = newrows[i_comb][itotcap] + int(row[icap])
		    	combnvio = row[invio] + ', ' + newrows[i_comb][invio]
		    	newrows[i_comb][invio] = combnvio
		    	combnhaz = row[inhaz] + ', ' + newrows[i_comb][inhaz]
		    	newrows[i_comb][inhaz] = combnhaz
		    	combncri = row[incri] + ', ' + newrows[i_comb][incri]
		    	newrows[i_comb][incri] = combncri
		    	combngen = row[ingen] + ', ' + newrows[i_comb][ingen]
		    	newrows[i_comb][ingen] = combngen
		    	combnvis = row[invis] + ', ' + newrows[i_comb][invis]
		    	newrows[i_comb][invis] = combnvis
		    	# combine numbers in string for now
		    	
		    	if int(row[invis]) is not 0:
		    		combviopervis = "{:.2f}".format(float(row[invio])/float(row[invis])) + ', ' + newrows[i_comb][iviopervis]
		    	else:
		    		combviopervis = 'No Visits' + ', ' + newrows[i_comb][iviopervis]
		    	newrows[i_comb][iviopervis] = combviopervis

		    	if int(row[invis]) is not 0:
		    		combhazpervis = "{:.2f}".format(float(row[inhaz])/float(row[invis])) + ', ' + newrows[i_comb][ihazpervis]
		    	else:
		    		combhazpervis = 'No Visits' + ', ' + newrows[i_comb][ihazpervis]
		    	newrows[i_comb][ihazpervis] = combhazpervis

	nname = filename[:-4] + "_combinedaddress.csv" # The filename of the output file
	header.append('Violations_Per_Visit')
	header.append('Hazard_Per_Visit')
	header.append('Total_Maximum_Capacity')
	
	with open(nname, "wb") as output_file:
		writer = csv.writer(output_file)
		writer.writerow(header)
		writer.writerows(newrows)
	return nname

def main():
	fname = sys.argv[1]
	nname = combine_same(fname)
	return nname
if __name__ == '__main__':
	main()