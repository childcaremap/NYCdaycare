import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='password',
    db='daycare')
cur = mydb.cursor()
cur.execute('SELECT * FROM BasicSum')

#info = csv.writer(file('../python_scraper/BasicInfoSum_2014_06_12.csv'))
csv_writer = csv.writer(open("BasicInfoSum_2014_06_12.csv", "wb"))
csv_writer.writerow([i[0] for i in cur.description]) # write headers
csv_writer.writerows(cur)
del csv_writer # this will close the CSV file
#mydb.commit()
cur.close()
print "Done"