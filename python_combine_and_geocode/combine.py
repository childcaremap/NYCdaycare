#filename = '04apr2014'
import sys
import csv

def combine_same(filename):
	print 'test'
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

		newrows = []  # Initialize clean rows
		address = []  # Initialize address / zip tupels
		# add entry only if address hasn't been added yet
		for row in info:
		    if (row[iaddress], row[izip]) not in address:
		        address.append((row[iaddress], row[izip]))
		        # Ruby scraper exports the csv with comma at the and causing an empty column at the end that needs to be removed
		        newrows.append(row[:-1])
		        ind = len(newrows)-1
		        newrows[ind].append(int(row[icap]))
		    else:
		    	i_comb = address.index((row[iaddress], row[izip]))
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
		    	newrows[i_comb][-1] = newrows[i_comb][-1] + int(row[icap])

	nname = filename[:-4] + "_combinedaddress.csv" # The filename of the output file
	header.append('Total Maximum Capacity')
	with open(nname, "wb") as output_file:
		writer = csv.writer(output_file)
		writer.writerow(header)
		writer.writerows(newrows)

def main():
	fname = sys.argv[1]
	combine_same(fname)

if __name__ == '__main__':
	main()