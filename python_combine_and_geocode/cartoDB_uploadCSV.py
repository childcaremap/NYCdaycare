#-------------------------------------------------------------------------------
# Created:     01/07/2014
# Copyright:   (c) Pedro 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#from cartodb import CartoDBOAuth, CartoDBException
from secret import *
import csv
import re
from cartodb import CartoDBOAuth, CartoDBException
from secret import *

cl = CartoDBOAuth(CONSUMER_KEY, CONSUMER_SECRET, user, password, cartodb_domain)

fname = 'BasicInfo_2014_06_09.csv'

meas = "site_id, center_name, permit_holder, address, borough, zip_code, phone, permit_number, permit_expiration_date, permit_status, age_range, maximum_capacity, certified_to_administer_medication, site_type"

with open(fname) as csvfile:
    bdat = csv.reader(csvfile)

    to_db = [(rw[0], rw[1], rw[2], rw[3], rw[4], rw[5], rw[6], rw[7], rw[8], rw[9], rw[10], rw[11], rw[12], rw[13]) for rw in bdat]
    del(to_db[0]) # remove first line of headers

    to_db = to_db[0:15]

    # Format as string for insert statement
    data = ','.join(str(en) for en in to_db)
    data =  re.sub(r'\'','"',str(data))
    data = re.sub(r'""','"', str(data))
    data = re.sub(r'" ','', str(data))
    data = re.sub(r'"','\'', str(data))

    # The SQL insert statement
    insert = "INSERT INTO basicinfo_test (%s) (VALUES %s)" % (meas, data)

    try:
        print cl.sql(insert)
    except CartoDBException as e:
        print ("some error ocurred", e)


