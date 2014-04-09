import csv

fname = "daycarenyc_2014_03_21.csv"  # The file we want to clean
nname = "clean_" + fname  # The filename of the cleaned file

rows = csv.reader(open(fname, "rb"))  # Open to-be-cleaned csv-file
newrows = []  # Initialize clean rows
address = []  # Initialize address / zip tupels

# add entry only if address hasn't been added yet
for row in rows:
    if (row[1], row[2]) not in address:
        address.append((row[1], row[2]))
        newrows.append(row)

writer = csv.writer(open(nname, "wb"))  # Open new csv file
writer.writerows(newrows)
