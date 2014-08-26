import sys
import MySQLdb
import re
import numpy as np

def average():
    mydb = MySQLdb.connect(host='localhost',
        user='root',
        passwd='password',
        db='daycare')
    with mydb:

        cur = mydb.cursor()

        #Add 2 more columns if necessary
        if cur.execute("SHOW COLUMNS FROM BasicSum WHERE Field = 'Mean_Violations_Per_Visit'") == 0:
            cur.execute("ALTER TABLE BasicSum ADD Mean_Violations_Per_Visit FLOAT")
        if cur.execute("SHOW COLUMNS FROM BasicSum WHERE Field = 'Score'") == 0:
            cur.execute("ALTER TABLE BasicSum ADD Score FLOAT")

        #insert mean number of violations per visit and weighted score
        cur.execute("SELECT SITE_ID, Number_Of_Violations, Hazard_Violations, Critical_Violations, General_Violations, Number_Of_Visits FROM BasicSum")
        
        rows = cur.fetchall()
        
        for row in rows:
            if row[5] != 0:
                cur.execute("UPDATE BasicSum SET Mean_Violations_Per_Visit = %s WHERE Site_ID = %s" , (float(row[1])/float(row[5]),row[0]))
                score = (3*float(row[2]) + 2*float(row[3]) + float(row[4]))/float(row[5])
                cur.execute("UPDATE BasicSum SET Score = %s WHERE Site_ID = %s" , (score,row[0]))
            
        mydb.commit()

    print "Done Averaging"

def main():
    average()

if __name__ == '__main__':
    main()