import time
time.clock()
import csv
#import mechanize
#from lxml import html, etree
#from StringIO import StringIO
#from lxml.html.soupparser import fromstring
import urllib2
from bs4 import BeautifulSoup
import re


outfile = open('Additional.csv','wb')
header = ['Facility ID','hours','removed','authorized','lastinspection','uncorrected']
writer = csv.writer(outfile)
writer.writerow(header)

outfile_comp = open('Compliance.csv','wb')
header_comp = ['Facility ID','Date','Regulation','Description','Status']
writer_comp = csv.writer(outfile_comp)
writer_comp.writerow(header_comp)

with open('home_basic_2015-02-01.csv','rU') as input_file:
    info = csv.reader(input_file)
    header = info.next()

    iid = header.index('Facility ID')
    ilink = header.index('Additional Information')

    for i,row in enumerate(info):
        if i >= 0:
            print i
            newrow = []
            newrow.append(row[iid])
            request = urllib2.Request(row[ilink])
            response = urllib2.urlopen(request)
            html = response.read()
            #with open("output2.txt","wb") as output_file:
            #   output_file.write(html)
            soup = BeautifulSoup(html)
            #find info about non-traditional hours
            tag =  soup.find(text=re.compile("Care available during non-traditional hours"))
            nontradhours = tag.next_element
            newrow.append(nontradhours)
            #find info about referral list
            tag =  soup.find(text=re.compile("Removed from referral list"))
            match = re.search(' No',tag.next_element)
            if match:
                removed = match.group()
            else:
                removed = tag.next_element.next_element.text
            newrow.append(removed)
            #find authorization info
            tag =  soup.find(text=re.compile("This facility is authorized"))
            authorized = tag
            newrow.append(authorized)
            #find date last inspected
            tag =  soup.find(text=re.compile("Date of Last Inspection"))
            lastinspection = tag.next_element.rstrip()
            newrow.append(lastinspection)
            #uncorrected violations
            tag =  soup.find(text=re.compile("Currently uncorrected violations"))
            uncorrected = tag.next_element.rstrip()
            newrow.append(uncorrected)

            writer.writerow(newrow)
            #time.sleep(.5)
            for viol in soup.find_all('tr',style='border-bottom: black solid thin;'):
                newrow = [row[iid]]
                for entry in viol.find_all('td'):
                    newrow.append(entry.text.encode('utf-8').strip())
                #print newrow
                writer_comp.writerow(newrow)

          
outfile.close()
outfile_comp.close()
time_elapsed = time.clock()
print [str(time_elapsed)+" seconds"]
print [str(time_elapsed/60)+" minutes"]

