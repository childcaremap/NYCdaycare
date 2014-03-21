child-care-map/NYCmap
==============
Project to map licensed day care centers for children 0-5 years in New York City.

Data from Bureau of Child Care at https://a816-healthpsi.nyc.gov/ChildCare/ChildCareList.do

Last updated CSV with scraped data (March 21, 2014): http://www.developeraccount.com/betanyc/daycarenyc.csv

Plan is to map the daycare centers, provide basic information (phone number, capacity, age range, etc) and summarize health inspection results.

Possible approaches to get data:

1. scrape data off website, quick and dirty. might not be sustainable
2. push the release of the data on the NYC Open Data site by bumping a request placed a year ago here: https://nycopendata.socrata.com/nominate/2570
3. contact the Department of Health and Mental Hygiene and ask for the data to be released via NYC Open Data: waiting for reply from Commissioner Mary Travis Bassett, M.D., MPH

==- NOTICE -==

The scrape script was made very quickly, so there are a few things to notice:
1. The data will be written to daycarenyc.csv by appending to the file. So after the script cycle is done and you would want to start a new cycle, you must first empty daycarenyc.csv
2. Browser based only. Cannot be run from commandline or with cron.
3. Please respect the 5 seconds interval so as not to hammer the https://a816-healthpsi.nyc.gov site, and don't run this every day

==- USAGE -==

1. Upload cookie.txt, daycare.php and daycarenyc.csv to your server of local environment
2. Make sure cookie.txt and daycarenyc.csv are writable
3. In your browser open daycare.php -> keep it open until you see "ready". It will reload every 5 seconds until it has retrieved all the pages.
