import sys
import MySQLdb
import re
import numpy as np

def rank():
    mydb = MySQLdb.connect(host='localhost',
        user='root',
        passwd='password',
        db='daycare')
    with mydb:

        cur = mydb.cursor()
        
        #Add 2 more columns if necessary
        if cur.execute("SHOW COLUMNS FROM BasicSum WHERE Field = 'Mean_Rank'") != 0:
            cur.execute("ALTER TABLE BasicSum DROP Mean_Rank")
        cur.execute("ALTER TABLE BasicSum ADD Mean_Rank INT")

        if cur.execute("SHOW COLUMNS FROM BasicSum WHERE Field = 'Mean_Cat'") != 0:
            cur.execute("ALTER TABLE BasicSum DROP Mean_Cat")
        cur.execute("ALTER TABLE BasicSum ADD Mean_Cat VARCHAR(10)")

        #Add 2 more columns if necessary
        if cur.execute("SHOW COLUMNS FROM BasicSum WHERE Field = 'Score_Rank'") != 0:
            cur.execute("ALTER TABLE BasicSum DROP Score_Rank")
        cur.execute("ALTER TABLE BasicSum ADD Score_Rank INT")

        if cur.execute("SHOW COLUMNS FROM BasicSum WHERE Field = 'Score_Cat'") != 0:
            cur.execute("ALTER TABLE BasicSum DROP Score_Cat")
        cur.execute("ALTER TABLE BasicSum ADD Score_Cat VARCHAR(10)")
            

        #select mean number of violations per visit
        cur.execute("SELECT SITE_ID, Mean_Violations_Per_Visit, Score FROM BasicSum")
        rows = cur.fetchall()
        matrix = np.asarray(rows)
        means = np.asarray(matrix[:,1],dtype=np.float64)
        scores = np.asarray(matrix[:,2],dtype=np.float64)

        means_nonan = np.delete(means,np.nonzero(np.isnan(means)==True))
        scores_nonan = np.delete(scores,np.nonzero(np.isnan(scores)==True))
        
        temp = means.argsort()
        meanranks = np.empty(len(means), int)
        meanranks[temp] = np.arange(len(means))

        temp = scores.argsort()
        scoreranks = np.empty(len(scores), int)
        scoreranks[temp] = np.arange(len(scores))

        quantile_means = np.percentile(means_nonan,(5,15,30,60,85,95))
        f = open('quantiles_means.txt', 'w')
        f.write('cdfs: ' + str([5,15,30,60,85,95]) + '\n')
        f.write('quantiles: ' + str(quantile_means))
        f.close()

        quantile_scores = np.percentile(scores_nonan,(5,15,30,60,85,95))
        f = open('quantiles_scores.txt', 'w')
        f.write('cdfs: ' + str([5,15,30,60,85,95]) + '\n')
        f.write('quantiles: ' + str(quantile_scores))
        f.close()

        for i,site in enumerate(matrix[:,0]):
            if ~np.isnan(means[i]):
                cur.execute("UPDATE BasicSum SET Mean_Rank = %s WHERE Site_ID = %s" , (meanranks[i],site))

                if means[i] <= quantile_means[0]:
                    cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('Top 5%',site))
                elif means[i] > quantile_means[0] and means[i] <= quantile_means[1]:
                    cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('Top 15%',site))
                elif means[i] > quantile_means[1] and means[i] <= quantile_means[2]:
                    cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('Top 30%',site))
                elif means[i] > quantile_means[3] and means[i] <= quantile_means[4]:
                    cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('Bottom 30%',site))
                elif means[i] > quantile_means[4] and means[i] <= quantile_means[5]:
                    cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('Bottom 15%',site))
                elif means[i] > quantile_means[5]:
                    cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('Bottom 5%',site))
                else:
                    cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('Average',site))
            else:
                cur.execute("UPDATE BasicSum SET Mean_Cat = %s WHERE Site_ID = %s" , ('No Data',site))

            if ~np.isnan(scores[i]):
                cur.execute("UPDATE BasicSum SET Score_Rank = %s WHERE Site_ID = %s" , (scoreranks[i],site))

                if scores[i] <= quantile_scores[0]:
                    cur.execute("UPDATE BasicSum SET Score_Cat = %s WHERE Site_ID = %s" , ('Top 5%',site))
                elif scores[i] > quantile_scores[0] and scores[i] <= quantile_scores[1]:
                    cur.execute("UPDATE BasicSum SET Score_Cat = %s WHERE Site_ID = %s" , ('Top 15%',site))
                elif scores[i] > quantile_scores[1] and scores[i] <= quantile_scores[2]:
                    cur.execute("UPDATE BasicSum SET Score_Cat = %s WHERE Site_ID = %s" , ('Top 30%',site))
                elif scores[i] > quantile_scores[3] and scores[i] <= quantile_scores[4]:
                    cur.execute("UPDATE BasicSum SET Score_Cat = %s WHERE Site_ID = %s" , ('Bottom 30%',site))
                elif scores[i] > quantile_scores[4] and scores[i] <= quantile_scores[5]:
                    cur.execute("UPDATE BasicSum SET Score_Cat = %s WHERE Site_ID = %s" , ('Bottom 15%',site))
                elif scores[i] > quantile_scores[5]:
                    cur.execute("UPDATE BasicSum SET Score_Cat = %s WHERE Site_ID = %s" , ('Bottom 5%',site))
                else:
                    cur.execute("UPDATE BasicSum SET Score_Cat = %s WHERE Site_ID = %s" , ('Average',site))
            else:
                cur.execute("UPDATE BasicSum SET Score_Cat = %s WHERE Site_ID = %s" , ('No Data',site))
            
        mydb.commit()

    print "Done Ranking"

def main():
    rank()

if __name__ == '__main__':
    main()