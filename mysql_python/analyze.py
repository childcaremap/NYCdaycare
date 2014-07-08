import MySQLdb
import re

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='password',
    db='daycare')
with mydb:

    cur = mydb.cursor()

    #Make new table and add a column
    cur.execute('DROP TABLE IF EXISTS BasicSum')
    cur.execute("CREATE TABLE BasicSum LIKE Basic")
    cur.execute("INSERT BasicSum SELECT * FROM Basic")
    cur.execute("ALTER TABLE BasicSum ADD Number_Of_Violations INT")
    #insert sum of violations for each site
    cur.execute("SELECT SITE_ID, COUNT(Violation_Category) FROM Inspections WHERE Violation_Category != '' GROUP BY Site_ID")
    rows = cur.fetchall()
    for row in rows:
        cur.execute("UPDATE BasicSum SET Number_Of_Violations = %s WHERE Site_ID = %s" , (row[1],row[0]))
    #Make NULL values into 0s
    cur.execute("UPDATE BasicSum SET Number_Of_Violations = 0 WHERE Number_Of_Violations IS NULL")
    mydb.commit()
    #Add another column
    cur.execute("ALTER TABLE BasicSum ADD Number_Of_Visits INT")
    #insert number of visits per site
    cur.execute("SELECT SITE_ID, COUNT(Visit_Date) FROM InspectionSum WHERE Visit_Date != 'No visit found in database.' GROUP BY Site_ID")
    rows = cur.fetchall()
    for row in rows:
        cur.execute("UPDATE BasicSum SET Number_Of_Visits = %s WHERE Site_ID = %s" , (row[1],row[0]))
    cur.execute("UPDATE BasicSum SET Number_Of_Visits = 0 WHERE Number_Of_Visits IS NULL")
    mydb.commit()

print "Done"