import sys
import csv
import numpy as np

def combine_same(filename):
	
	info = csv.reader(file(filename))
	header = info.next()
	#imedvio = header.index('Median_Violations_Per_Visit')
	imeavio = header.index('Mean_Violations_Per_Visit')
	iscore = header.index('Score')
	nrows = 0
	for row in info:
	    if row[imeavio] != '':
	    	nrows += 1
	    
	info = csv.reader(file(filename))
	header = info.next()

	A_mea = np.zeros((nrows,1))
	A_score = np.zeros((nrows,1))
	nrows = 0
	i = 0
	for row in info:
	    if row[imeavio] != '':
	    	A_mea[i] = float(row[imeavio])
	    	A_score[i] = float(row[iscore])
	    	i += 1

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
	 	imearan = header.index('Mean_Rank')
	 	iscoran = header.index('Score_Rank')
	 	imeacat = header.index('Mean_Cat')
	 	iscocat = header.index('Score_Cat')
	 	
	 	inpermits = len(header)
	 	iavmeavio = len(header)+1
	 	iavscore = len(header)+2
	 	

		newrows = []  # Initialize clean rows
		address = []  # Initialize address / zip tupels
		# add entry only if address hasn't been added yet
		for row in info:
		    if (row[iaddress], row[izip]) not in address:
		        address.append((row[iaddress], row[izip]))
		        newrows.append(row)
		        ind = len(newrows)-1
		        if row[imeavio] != '':
		        	newrows[ind].append(1)
		        	newrows[ind].append(row[imeavio])
		        	newrows[ind].append(row[iscore])
		        else:
		        	newrows[ind].append(1)
		        	newrows[ind].append(np.median(A_mea))
		        	newrows[ind].append(np.median(A_score))
		    else:
		    	i_comb = address.index((row[iaddress], row[izip]))
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
		    	combmeavio = row[imeavio] + ' / ' + newrows[i_comb][imeavio]
		    	newrows[i_comb][imeavio] = combmeavio
		    	combscore = row[iscore] + ' / ' + newrows[i_comb][iscore]
		    	newrows[i_comb][iscore] = combscore
		    	combmearan = row[imearan] + ' / ' + newrows[i_comb][imearan]
		    	newrows[i_comb][imearan] = combmearan
		    	combscoran = row[iscoran] + ' / ' + newrows[i_comb][iscoran]
		    	newrows[i_comb][iscoran] = combscoran
		    	combmeacat = row[imeacat] + ' / ' + newrows[i_comb][imeacat]
		    	newrows[i_comb][imeacat] = combmeacat
		    	combscocat = row[iscocat] + ' / ' + newrows[i_comb][iscocat]
		    	newrows[i_comb][iscocat] = combscocat

		    	if row[imeavio] != '':
		    		if newrows[i_comb][iavmeavio] != '':
		    			newrows[i_comb][iavmeavio] = (float(row[imeavio]) + newrows[i_comb][inpermits]*float(newrows[i_comb][iavmeavio]))/(newrows[i_comb][inpermits] + 1)
		    			newrows[i_comb][inpermits] += 1
		    	else:
		    		newrows[i_comb][iavmeavio] =  (np.median(A_mea) + newrows[i_comb][inpermits]*float(newrows[i_comb][iavmeavio]))/(newrows[i_comb][inpermits] + 1)
		    		newrows[i_comb][inpermits] += 1

		    	if row[iscore] != '':
		    		if newrows[i_comb][iavscore] != '':
		    			newrows[i_comb][iavscore] = (float(row[iscore]) + newrows[i_comb][inpermits]*float(newrows[i_comb][iavscore]))/(newrows[i_comb][inpermits] + 1)
		    			newrows[i_comb][inpermits] += 1
		    	else:
		    		newrows[i_comb][iavscore] =  (np.median(A_mea) + newrows[i_comb][inpermits]*float(newrows[i_comb][iavscore]))/(newrows[i_comb][inpermits] + 1)
		    		newrows[i_comb][inpermits] += 1

	nname = filename[:-4] + "_combinedaddress.csv" # The filename of the output file
	#header.append('Violations_Per_Visit')
	#header.append('Hazard_Per_Visit')
	#header.append('Total_Maximum_Capacity')
	header.append('Number_Of_Permits')
	header.append('Average_Mean_Violations_Per_Visit')
	header.append('Average_Score')
	
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