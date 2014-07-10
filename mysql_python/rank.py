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
    mindate =  '2012-6-12'

    #Add 2 more columns
    if cur.execute("SHOW COLUMNS FROM BasicSum WHERE Field = 'Median_Rank'") != 0:
        cur.execute("ALTER TABLE BasicSum DROP Median_Rank")
    cur.execute("ALTER TABLE BasicSum ADD Median_Rank INT")
    
    if cur.execute("SHOW COLUMNS FROM BasicSum WHERE Field = 'Mean_Rank'") != 0:
        cur.execute("ALTER TABLE BasicSum DROP Mean_Rank")
    cur.execute("ALTER TABLE BasicSum ADD Mean_Rank INT")

    if cur.execute("SHOW COLUMNS FROM BasicSum WHERE Field = 'Median_Cat'") != 0:
        cur.execute("ALTER TABLE BasicSum DROP Median_Cat")
    cur.execute("ALTER TABLE BasicSum ADD Median_Cat VARCHAR(10)")

    if cur.execute("SHOW COLUMNS FROM BasicSum WHERE Field = 'Mean_Cat'") != 0:
        cur.execute("ALTER TABLE BasicSum DROP Mean_Cat")
    cur.execute("ALTER TABLE BasicSum ADD Mean_Cat VARCHAR(10)")
        

    #insert median and mean number of violations per visit
    #cur.execute("SELECT SITE_ID, Visit_Date, COUNT(Violation_Category) FROM Inspections WHERE Violation_Category != '' AND Visit_Date >  %s GROUP BY Site_ID, Visit_Date", (mindate,))
    cur.execute("SELECT SITE_ID, Median_Violations_Per_Visit, Mean_Violations_Per_Visit FROM BasicSum")
    rows = cur.fetchall()
    matrix = np.asarray(rows)
    medians = np.asarray(matrix[:,1],dtype=np.float64)
    means = np.asarray(matrix[:,2],dtype=np.float64)

    medians_nonan = np.delete(medians,np.nonzero(np.isnan(medians)==True))
    means_nonan = np.delete(means,np.nonzero(np.isnan(means)==True))
    
    temp = medians.argsort()
    medianranks = np.empty(len(medians), int)
    medianranks[temp] = np.arange(len(medians))

    temp = means.argsort()
    meanranks = np.empty(len(means), int)
    meanranks[temp] = np.arange(len(means))

    quantile_medians = np.percentile(medians_nonan,(25,75,90,95))
    quantile_means = np.percentile(means_nonan,(25,75,90,95))
    for i,site in enumerate(matrix[:,0]):
        if ~np.isnan(medians[i]):
            cur.execute("UPDATE BasicSum SET Median_Rank = %s WHERE Site_ID = %s" , (medianranks[i],site))
            cur.execute("UPDATE BasicSum SET Mean_Rank = %s WHERE Site_ID = %s" , (meanranks[i],site))
            if medians[i] <= quantile_medians[0]:
                cur.execute("UPDATE BasicSum SET Median_Cat = %s WHERE Site_ID = %s" , ('Top 25%',site))
            elif medians[i] >= quantile_medians[1] and medians[i] < quantile_medians[2]:
                cur.execute("UPDATE BasicSum SET Median_Cat = %s WHERE Site_ID = %s" , ('Bottom 25%',site))
            elif medians[i] >= quantile_medians[2] and medians[i] < quantile_medians[3]:
                cur.execute("UPDATE BasicSum SET Median_Cat = %s WHERE Site_ID = %s" , ('Bottom 10%',site))
            elif medians[i] >= quantile_medians[3]:
                cur.execute("UPDATE BasicSum SET Median_Cat = %s WHERE Site_ID = %s" , ('Bottom 5%',site))
            else:
                cur.execute("UPDATE BasicSum SET Median_Cat = %s WHERE Site_ID = %s" , ('Average',site))

            if means[i] <= quantile_means[0]:
                cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('Top 25%',site))
            elif means[i] >= quantile_means[1] and means[i] < quantile_means[2]:
                cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('Bottom 25%',site))
            elif means[i] >= quantile_means[2] and means[i] < quantile_means[3]:
                cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('Bottom 10%',site))
            elif means[i] >= quantile_means[3]:
                cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('Bottom 5%',site))
            else:
                cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('Average',site))
        else:
            cur.execute("UPDATE BasicSum SET Median_Cat = %s WHERE Site_ID = %s" , ('No Data',site))
            cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('No Data',site))
        
    mydb.commit()

print "Done"