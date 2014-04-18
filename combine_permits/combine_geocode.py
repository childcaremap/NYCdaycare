filename = '04apr2014_combinedaddress'

import csv
import time
from pygeocoder import Geocoder


with open(filename + '.csv', 'rb') as input_file:
	info = csv.reader(input_file)
	header = info.next()
	#iname = header.index('Center Name')
	#iholder = header.index('Permit Holder')
 	iaddress = header.index('Address')
 	iborough = header.index('Borough')
 	izip= header.index('Zip Code')
 	#iphone = header.index('Phone')
 	#ipermit = header.index('Permit Number')
 	#iexp = header.index('Permit Expiration Date')
 	#istatus = header.index('Permit Status')
 	#iagerange= header.index('Age Range')
 	#icap = header.index('Maximum Capacity')
 	#imed = header.index('Certified to Administer Medication')
 	#itype = header.index('Site Type')

 	k = 0
 	newrows = []  # Initialize clean rows
	# retrieve geolocation from Google API
	for i, row in enumerate(info):
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
				row[ilat] = result[0].coordinates[0]
				row[ilon] = result[0].coordinates[1]
				newrows.append(row)
		except:
			k = k + 1
			row.append('')
			row.append('')
			newrows.append(row)
	    
print str(k) + ' entries not geocoded'

nname = filename + "_geocoded.csv" # The filename of the output file
header.append('Lat')
header.append('Lon')
with open(nname, "wb") as output_file:
	writer = csv.writer(output_file)
	writer.writerow(header)
	writer.writerows(newrows)