from cartodb import CartoDBOAuth, CartoDBException
from secret import *
import csv
import re
import time

cl = CartoDBOAuth(CONSUMER_KEY, CONSUMER_SECRET, user, password, cartodb_domain)

with open('BasicInfo_2014_06_18_combinedaddress_geocoded_combinedgeo.csv', 'rb') as input_file:
    info = csv.reader(input_file)
    header = info.next()
    headernew = []
    for cell in header:
        cell =  re.sub(' ','_',str(cell))
        headernew.append(cell)
    column_names = '('+ str(headernew).strip('[]') + ')'
    column = re.sub('\'','',column_names)

    info_server = cl.sql('select ' + column + ' from basicinfo')
    output_file =  open('Serverdata.csv', "wb")
    writer = csv.writer(output_file)
    writer.writerow(header)
    for row in info_server["rows"]:
        rowwrite = []
        rowvalues = row.values()
        rowwrite = str(rowvalues[0]).strip('()').rsplit(',')
        writer.writerow(rowwrite)
    output_file.close()
