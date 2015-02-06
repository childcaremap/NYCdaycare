import sys
import csv

def remove_suspended(filename):
    with open(filename, 'rU') as input_file:
        info = csv.reader(input_file)
        header = info.next()

        istatus = header.index('Facility Status')

        newrows = []  # Initialize clean rows
        # add entry only if geolocation hasn't been added yet
        for row in info:
            if row[istatus] not in ('Suspended','Pending Denial','Pending Revocation','Pending Revocation and Denial'):
                newrows.append(row)
            else:
                print 'removed ' + str(row)


    nname = filename[:-4] + "_nosuspended.csv" # The filename of the output file
    with open(nname, "wb") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        writer.writerows(newrows)
    return nname

def main():
    fname = sys.argv[1]
    nname = remove_suspended(fname)
    return nname
    
if __name__ == '__main__':
    main()