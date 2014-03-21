child-care-map
==============
Project to map licensed day care centers for children 0-5 years in New York City.

Data retrieved from Bureau of Child Care at https://a816-healthpsi.nyc.gov/ChildCare/ChildCareList.do

Plan is to map the daycare centers, provide basic information (phone number, capacity, age range, etc) and summarize health inspection results.

==- NOTICE -==

The scrape script was made very quickly, so there are a few things to notice:
1. The data will be written to daycarenyc.csv by appending to the file. So after the script cycle is done and you would want to start a new cycle, you must first empty daycarenyc.csv
2. Browser based only. Cannot be run from commandline or with cron.

==- USAGE -==

1. Upload cookie.txt, daycare.php and daycarenyc.csv to your server of local environment
2. Make sure cookie.txt and daycarenyc.csv are writable
3. In your browser open daycare.php -> keep it open until you see "ready". It will reload every 5 seconds until it has retrieved all the pages.
