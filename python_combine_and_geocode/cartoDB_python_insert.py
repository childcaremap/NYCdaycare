from cartodb import CartoDBOAuth, CartoDBException
from secret import *
import csv
import re

cl = CartoDBOAuth(CONSUMER_KEY, CONSUMER_SECRET, user, password, cartodb_domain)

with open('BasicInfo_2014_05_30_combinedaddress_geocoded_combinedgeo.csv', 'rb') as input_file:
    info = csv.reader(input_file)
    header = info.next()
    for row in info:
        try:
            rownew = []
            for cell in row:
                cell =  re.sub(r'\'','"',str(cell))
                rownew.append(cell)
            writerow = '('+ str(rownew).strip('[]') + ')'
            print cl.sql('INSERT INTO nycdaycaremap values' + writerow)
        except CartoDBException as e:
            print ("some error ocurred", e)