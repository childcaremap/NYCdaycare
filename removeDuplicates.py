import csv

rows = csv.reader(open("daycarenyc_2014_03_21.csv", "rb"))
newrows = []
address = []
for row in rows:
    if (row[1], row[2]) not in address:
        address.append((row[1], row[2]))
        newrows.append(row)

writer = csv.writer(open("daycarenyc_clean_2014_03_21.csv", "wb"))
writer.writerows(newrows)
