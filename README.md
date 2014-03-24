child-care-map/NYCmap
=====================
Project to map licensed day care centers for children 0-5 years in New York City.

Data from Bureau of Child Care at https://a816-healthpsi.nyc.gov/ChildCare/ChildCareList.do

Last updated CSV with scraped data (March 21, 2014): http://www.developeraccount.com/betanyc/daycarenyc.csv

Plan is to map the daycare centers, provide basic information (phone number, capacity, age range, etc) and summarize health inspection results.

Possible approaches to get data:

1. scrape data off website, quick and dirty. might not be sustainable
2. push the release of the data on the NYC Open Data site by bumping a request placed a year ago here: https://nycopendata.socrata.com/nominate/2570
3. contact the Department of Health and Mental Hygiene and ask for the data to be released via NYC Open Data: waiting for reply from Commissioner Mary Travis Bassett, M.D., MPH

Approaches for Scraping:

1. php based scrape script in "scraper" folder working for first layer data (Service Name	Address	Zip Code	Phone	Permit Status) Note: do NOT run script without consulting with omnisite or schmiani! Data retrieved on March 21 2014 is saved on github.
2. python beautifulsoup cannot access data because it is loaded with javascript
3. python scrapy should work, schmiani is working on this approach

Cleaning Data:

Licenses are issued for 0-2 years or 2-5 years, therefore many child care centers are listed twice. Python cleaning script "removeDuplicates.py" removes all addresses that are listed twice, saves new .csv file with "clean_" prefix. Some child care centers use different addresses nearby, they are still represented twice. Some encoding issues in service names such as single and double quotes not converting properly still present. 
