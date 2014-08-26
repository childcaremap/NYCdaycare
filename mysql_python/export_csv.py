import sys 
import csv
import MySQLdb
import datetime

def export_csv(datescraped):
    mydb = MySQLdb.connect(host='localhost',
        user='root',
        passwd='password',
        db='daycare')
    cur = mydb.cursor()
    cur.execute('SELECT * FROM BasicSum')
    
    date = str(datescraped.isoformat())

    #info = csv.writer(file('../python_scraper/BasicInfoSum_2014_06_12.csv'))
    csv_writer = csv.writer(open("BasicInfoSum_"+ date + ".csv", "wb"))
    csv_writer.writerow([i[0] for i in cur.description]) # write headers
    csv_writer.writerows(cur)
    del csv_writer # this will close the CSV file
    #mydb.commit()
    cur.close()
    print "Done Exporting"

def main():
    # input date scrapes in Year-month-day or leave empty for today
    if len(sys.argv) > 1:
        datescraped = datetime.datetime.strptime(sys.argv[1], "%Y-%m-%d").date()
        print "Exporting data assumed it was scraped on " + str(datescraped.isoformat())
    else:
        datescraped = datetime.date.today()
        print "Exporting data assumed it was scraped today"
    export_csv(datescraped)

if __name__ == '__main__':
    main()