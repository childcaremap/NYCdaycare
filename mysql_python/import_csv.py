import csv
import MySQLdb
import re

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='password',
    db='daycare')
cur = mydb.cursor()
cur.execute('DROP TABLE IF EXISTS Basic')
cur.execute('DROP TABLE IF EXISTS Inspections')
cur.execute('DROP TABLE IF EXISTS InspectionSum')

info = csv.reader(file('../python_scraper/BasicInfo_2014_06_12.csv'))
header = info.next()
headersql = [s.replace(' ', '_') for s in header]

query = 'CREATE TABLE Basic('+'%s TEXT, ' * (len(header)-1)+'%s TEXT)'
query = query % tuple(headersql)
cur.execute(query)

query = 'INSERT INTO Basic(' + '%s, ' *(len(header)-1) + '%s)'
query = query % tuple(headersql)
query = query + ' VALUES(' + '%s, ' *(len(header)-1) + '%s)'
for row in info:
	cur.execute(query, row)

mydb.commit()

info = csv.reader(file('../python_scraper/InspectionInfo_2014_06_12.csv'))
header = info.next()
headersql = [s.replace(' ', '_').replace('-','_') for s in header]

query = 'CREATE TABLE Inspections('+'%s TEXT, ' * (len(header)-1)+'%s TEXT)'
query = query % tuple(headersql)
cur.execute(query)

query = 'INSERT INTO Inspections(' + '%s, ' *(len(header)-1) + '%s)'
query = query % tuple(headersql)
query = query + ' VALUES(' + '%s, ' *(len(header)-1) + '%s)'
for row in info:
    cur.execute(query, row)

mydb.commit()

info = csv.reader(file('../python_scraper/InspectionSummaries_2014_06_12.csv'))
header = info.next()
headersql = [s.replace(' ', '_').replace('-','_') for s in header]

query = 'CREATE TABLE InspectionSum('+'%s TEXT, ' * (len(header)-1)+'%s TEXT)'
query = query % tuple(headersql)
cur.execute(query)

query = 'INSERT INTO InspectionSum(' + '%s, ' *(len(header)-1) + '%s)'
query = query % tuple(headersql)
query = query + ' VALUES(' + '%s, ' *(len(header)-1) + '%s)'
for row in info:
    cur.execute(query, row)

mydb.commit()
cur.close()
print "Done"