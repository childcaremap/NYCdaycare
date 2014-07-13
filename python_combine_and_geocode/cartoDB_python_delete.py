from cartodb import CartoDBOAuth, CartoDBException
from secret import *

cl = CartoDBOAuth(CONSUMER_KEY, CONSUMER_SECRET, user, password, cartodb_domain)
try:
    print cl.sql("delete from basicinfo_test")
except CartoDBException as e:
    print ("some error ocurred", e)