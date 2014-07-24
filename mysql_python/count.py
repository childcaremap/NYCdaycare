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
    #Make new table
    cur.execute('DROP TABLE IF EXISTS BasicSum')
    cur.execute("CREATE TABLE BasicSum LIKE Basic")
    cur.execute("INSERT BasicSum SELECT * FROM Basic")
    #add a column
    cur.execute("ALTER TABLE BasicSum ADD Number_Of_Violations INT")
    #insert sum of violations for each site
    cur.execute("SELECT SITE_ID, COUNT(Violation_Category) FROM Inspections \
        WHERE Violation_Category != '' AND Visit_Date >  %s GROUP BY Site_ID", (mindate,))
    rows = cur.fetchall()
    for row in rows:
        cur.execute("UPDATE BasicSum SET Number_Of_Violations = %s WHERE Site_ID = %s" , (row[1],row[0]))
    #Make NULL values into 0s
    cur.execute("UPDATE BasicSum SET Number_Of_Violations = 0 WHERE Number_Of_Violations IS NULL")
    mydb.commit()

    #Add another column
    cur.execute("ALTER TABLE BasicSum ADD Hazard_Violations INT")

    #insert sum of PUBLIC HEALTH HAZARD violations for each site
    cur.execute("SELECT SITE_ID, COUNT(Violation_Category) FROM Inspections \
        WHERE Violation_Category = 'PUBLIC HEALTH HAZARD' AND Visit_Date > %s\
        GROUP BY Site_ID", (mindate,))
    rows = cur.fetchall()
    for row in rows:
        cur.execute("UPDATE BasicSum SET Hazard_Violations = %s WHERE Site_ID = %s" , (row[1],row[0]))
    #Make NULL values into 0s
    cur.execute("UPDATE BasicSum SET Hazard_Violations = 0 WHERE Hazard_Violations IS NULL")
    mydb.commit()

    #Add another column
    cur.execute("ALTER TABLE BasicSum ADD Critical_Violations INT")

    #insert sum of critical violations for each site
    cur.execute("SELECT SITE_ID, COUNT(Violation_Category) FROM Inspections \
        WHERE Violation_Category = 'CRITICAL' AND Visit_Date > %s\
        GROUP BY Site_ID", (mindate,))
    rows = cur.fetchall()
    for row in rows:
        cur.execute("UPDATE BasicSum SET Critical_Violations = %s WHERE Site_ID = %s" , (row[1],row[0]))
    #Make NULL values into 0s
    cur.execute("UPDATE BasicSum SET Critical_Violations = 0 WHERE Critical_Violations IS NULL")
    mydb.commit()

    #Add another column
    cur.execute("ALTER TABLE BasicSum ADD General_Violations INT")

    #insert sum of general violations for each site
    cur.execute("SELECT SITE_ID, COUNT(Violation_Category) FROM Inspections \
        WHERE Violation_Category = 'GENERAL' AND Visit_Date > %s\
        GROUP BY Site_ID", (mindate,))
    rows = cur.fetchall()
    for row in rows:
        cur.execute("UPDATE BasicSum SET General_Violations = %s WHERE Site_ID = %s" , (row[1],row[0]))
    #Make NULL values into 0s
    cur.execute("UPDATE BasicSum SET General_Violations = 0 WHERE General_Violations IS NULL")
    mydb.commit()

    #Add another column
    cur.execute("ALTER TABLE BasicSum ADD Number_Of_Visits INT")
    #insert number of visits per site
    cur.execute("SELECT SITE_ID, COUNT(Visit_Date) FROM InspectionSum \
        WHERE Visit_Date > %s \
        GROUP BY Site_ID", (mindate,))
    rows = cur.fetchall()
    for row in rows:
        cur.execute("UPDATE BasicSum SET Number_Of_Visits = %s WHERE Site_ID = %s" , (row[1],row[0]))
    cur.execute("UPDATE BasicSum SET Number_Of_Visits = 0 WHERE Number_Of_Visits IS NULL")
    mydb.commit()

print "Done"