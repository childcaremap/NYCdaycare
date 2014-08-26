import sys 
import csv
import MySQLdb
import numpy as np
import time
import datetime

def import_csv(datescraped):
    mydb = MySQLdb.connect(host='localhost',
        user='root',
        passwd='password',
        db='daycare')
    cur = mydb.cursor()
    # drop tables and create them new
    cur.execute('DROP TABLE IF EXISTS Basic')
    cur.execute('DROP TABLE IF EXISTS Inspections')
    cur.execute('DROP TABLE IF EXISTS InspectionSum')

    date = str(datescraped.isoformat())
    # read in basic data and put into mysql table
    # get size of table
    info = csv.reader(file('../python_scraper/BasicInfo_' + date + '.csv'))
    header = info.next()
    nrows = 0
    for row in info:
        nrows = nrows+1
    ncols = len(row)
    L = np.zeros((nrows,ncols))

    # get maximum width of columns in table
    info = csv.reader(file('../python_scraper/BasicInfo_' + date + '.csv'))
    header = info.next()
    for i,row in enumerate(info):
        for j,cell in enumerate(row):
            L[i,j] = len(cell)

    maxwidth = L.max(0)

    # read in data and put into table
    info = csv.reader(file('../python_scraper/BasicInfo_' + date + '.csv'))
    header = info.next()
    headersql = [s.replace(' ', '_') for s in header]

    querylist = []
    idate = []
    for i in range(ncols):
        if header[i].lower().find('date') == -1:
            querylist.append(headersql[i] + ' VARCHAR(' + str(int(maxwidth[i])) + ')')
        else:
            idate = i
            querylist.append(headersql[i] + ' DATE')

    query = 'CREATE TABLE Basic(' + ",".join(querylist) + ')'
    cur.execute(query)

    query = 'INSERT INTO Basic(' + '%s, ' *(len(header)-1) + '%s)'
    query = query % tuple(headersql)
    query = query + ' VALUES(' + '%s, ' *(len(header)-1) + '%s)'
    for row in info:
        row[idate] = time.strftime("%Y-%m-%d",time.strptime(row[idate],"%m/%d/%Y"))
        cur.execute(query, row)

    mydb.commit()


    # read in inspection details and put into mysql table
    # get size of table
    info = csv.reader(file('../python_scraper/InspectionInfo_' + date + '.csv'))
    header = info.next()
    nrows = 0
    for row in info:
        nrows = nrows+1
    ncols = len(row)
    L = np.zeros((nrows,ncols))

    # get maximum width of columns in table
    info = csv.reader(file('../python_scraper/InspectionInfo_' + date + '.csv'))
    header = info.next()
    for i,row in enumerate(info):
        for j,cell in enumerate(row):
            L[i,j] = len(cell)
    maxwidth = L.max(0)

    # read in data and put into table
    info = csv.reader(file('../python_scraper/InspectionInfo_' + date + '.csv'))
    header = info.next()
    headersql = [s.replace(' ', '_').replace('-','_') for s in header]

    querylist = []
    for i in range(ncols):
        if header[i].lower().find('date') == -1:
            querylist.append(headersql[i] + ' VARCHAR(' + str(int(maxwidth[i])) + ')')
        else:
            idate = i
            querylist.append(headersql[i] + ' DATE')

    query = 'CREATE TABLE Inspections(' + ",".join(querylist) + ')'
    cur.execute(query)

    query = 'INSERT INTO Inspections(' + '%s, ' *(len(header)-1) + '%s)'
    query = query % tuple(headersql)
    query = query + ' VALUES(' + '%s, ' *(len(header)-1) + '%s)'
    for row in info:
        row[idate] = time.strftime("%Y-%m-%d",time.strptime(row[idate],"%m/%d/%Y"))
        cur.execute(query, row)

    mydb.commit()

    # read in inspection summery and put into mysql table
    # get size of table
    info = csv.reader(file('../python_scraper/InspectionSummaries_' + date + '.csv'))
    header = info.next()
    nrows = 0
    for row in info:
        nrows = nrows+1
    ncols = len(row)
    L = np.zeros((nrows,ncols))

    # get maximum width of columns in table
    info = csv.reader(file('../python_scraper/InspectionSummaries_' + date + '.csv'))
    header = info.next()
    for i,row in enumerate(info):
        for j,cell in enumerate(row):
            L[i,j] = len(cell)
    maxwidth = L.max(0)

    # read in data and put into table
    info = csv.reader(file('../python_scraper/InspectionSummaries_' + date + '.csv'))
    header = info.next()
    headersql = [s.replace(' ', '_').replace('-','_') for s in header]

    querylist = []
    for i in range(ncols):
        if header[i].lower().find('date') == -1:
            querylist.append(headersql[i] + ' VARCHAR(' + str(int(maxwidth[i])) + ')')
        else:
            idate = i
            querylist.append(headersql[i] + ' DATE')

    query = 'CREATE TABLE InspectionSum(' + ",".join(querylist) + ')'
    cur.execute(query)

    query = 'INSERT INTO InspectionSum(' + '%s, ' *(len(header)-1) + '%s)'
    query = query % tuple(headersql)
    query = query + ' VALUES(' + '%s, ' *(len(header)-1) + '%s)'
    for row in info:
        if row[idate] != 'No visit found in database.':
            row[idate] = time.strftime("%Y-%m-%d",time.strptime(row[idate],"%m/%d/%Y"))
            cur.execute(query, row)

    mydb.commit()

    #close mysql cursor
    cur.close()
    print "Done Importing"

def main():
    # input date scrapes in Year-month-day or leave empty for today
    if len(sys.argv) > 1:
        datescraped = datetime.datetime.strptime(sys.argv[1], "%Y-%m-%d").date()
        print "Importing data scraped on " + sys.argv[1]
    else:
        datescraped = datetime.date.today()
        print "Importing data scraped today"
    import_csv(datescraped)

if __name__ == '__main__':
    main()