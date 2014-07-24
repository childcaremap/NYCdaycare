import MySQLdb
import re
import numpy as np

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='password',
    db='daycare')
with mydb:

    cur = mydb.cursor()

    # 2 years prior to scrape date
    mindate =  '2012-7-23'

    #Add 2 more columns if necessary
    #if cur.execute("SHOW COLUMNS FROM BasicSum WHERE Field = 'Median_Violations_Per_Visit'") == 0:
    #    cur.execute("ALTER TABLE BasicSum ADD Median_Violations_Per_Visit FLOAT")
    
    if cur.execute("SHOW COLUMNS FROM BasicSum WHERE Field = 'Mean_Violations_Per_Visit'") == 0:
        cur.execute("ALTER TABLE BasicSum ADD Mean_Violations_Per_Visit FLOAT")

    #insert median and mean number of violations per visit
    #cur.execute("SELECT SITE_ID, Visit_Date, COUNT(Violation_Category) FROM Inspections WHERE Violation_Category != '' AND Visit_Date >  %s GROUP BY Site_ID, Visit_Date", (mindate,))
    cur.execute("SELECT SITE_ID, Visit_Date, \
        COUNT(IF(Violation_Category != '',1,NULL)) \
        FROM Inspections \
        WHERE Visit_Date >  %s GROUP BY Site_ID, Visit_Date", (mindate,))
    rows = cur.fetchall()
    LastID = []
    nviol = []
    for row in rows:
        if LastID == []:
            LastID = row[0]
            nviol = [row[2]]
        elif row[0] != LastID:
            #median = np.median(np.array(nviol))
            mean = np.mean(np.array(nviol))
            #cur.execute("UPDATE BasicSum SET Median_Violations_Per_Visit = %s WHERE Site_ID = %s" , (median,LastID))
            cur.execute("UPDATE BasicSum SET Mean_Violations_Per_Visit = %s WHERE Site_ID = %s" , (mean,LastID))
            np.array(nviol)
            LastID = row[0]
            nviol = [row[2]]
        elif row[0] == LastID:
            nviol.append(row[2]) 

        #cur.execute("UPDATE BasicSum SET Median_Violations_Per_Visit = %s WHERE Site_ID = %s" , (row[1],row[0]))
    #Make NULL values into 0s
    #cur.execute("UPDATE BasicSum SET Median_Violations_Per_Visit = 0 WHERE Median_Violations_Per_Visit IS NULL AND Number_Of_Visits != 0")
    cur.execute("UPDATE BasicSum SET Mean_Violations_Per_Visit = 0 WHERE Mean_Violations_Per_Visit IS NULL AND Number_Of_Visits != 0")
    mydb.commit()

print "Done"