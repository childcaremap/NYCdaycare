from pygeocoder import Geocoder
f = open('geofile.txt','w')
results = Geocoder.geocode("2 SOUTH END AVENUE, 10280 NEW YORK")
f.write(str(results[0].coordinates))
f.close()