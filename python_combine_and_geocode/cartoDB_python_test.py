from cartodb import CartoDBOAuth, CartoDBException
from secret import *
import json

cl = CartoDBOAuth(CONSUMER_KEY, CONSUMER_SECRET, user, password, cartodb_domain)
try:
    a = cl.sql("SELECT * FROM basicinfo WHERE site_id='DC20687'")   # WHERE site_id='DC20687'

    print(a)

    #for key, value in a.items():
        #print(key, value)
except CartoDBException as e:
    print ("some error ocurred", e)