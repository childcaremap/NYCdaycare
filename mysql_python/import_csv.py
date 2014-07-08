import csv
import MySQLdb
import re

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='password',
    db='daycare')
cur = mydb.cursor()
cur.execute('DROP TABLE IF EXISTS Basic')


info = csv.reader(file('../python_combine_and_geocode/BasicInfo_2014_06_12.csv'))
header = info.next()
headersql = [s.replace(' ', '_') for s in header]

query = 'CREATE TABLE Basic('+'%s VARCHAR(255), ' * (len(header)-1)+'%s VARCHAR(255))'
query = query % tuple(headersql)
cur.execute(query)

query = 'INSERT INTO Basic(' + '%s, ' *(len(header)-1) + '%s)'
query = query % tuple(headersql)
query = query + ' VALUES(' + '%s, ' *(len(header)-1) + '%s)'
for row in info:
	cur.execute(query, row)

mydb.commit()
cur.close()
print "Done"