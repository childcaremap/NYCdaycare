=====================
childcaremap/NYCdaycare
=====================
Project to map licensed day care centers specifically for children 0-5 years in New York City.

Data from NYC Department of Health and Mental Hygiene:

1. Center-based child care at https://a816-healthpsi.nyc.gov/ChildCare/ChildCareList.do
2. Home-based child care at http://it.ocfs.ny.gov/ccfs_facilitysearch/

Located home-based child care information for download (or API access) on NY State Open Data Portal: https://data.ny.gov/Human-Services/Child-Care-Regulated-Programs/cb42-qumz

Current status is that we map the daycare centers, provide basic information (phone number, capacity, age range, etc) and we provide filter options. Ranking based on summarization of health inspection results is  work in progress.

Attempts to get data released though NYC Open Data Portal failed, therefore we are scraping the data where necessary (basic information for home-based day cares is available, see above).

We are using python package mechanize, the code is in folder "python_scraper"

Older versions of scrapers, not used anymore:
  
2. ruby based script with mechanize in folder "ruby_scraper"
3. php based script in folder "php_scraper"

Combining permits:

Group-based child care permits are issued for 0-2 years or 2-5 years, therefore many child care centers are listed twice (or more times, if they have different types of premits, such as private and corporate etc.). Also, sometimes more than one daycare center are located at the same address. Because they have the same geolocation, only one of the entries will be visible in a map (unless artificial jitter is introduced, an approach not taken here). Python scripts in folder "python_combine_and_geocode" combines any permit at the same location into one entry, but preserves the different entries with slashes. This is done just for mapping, the original file is kept separately. Workflow is to combine permits for the exact same address, then geocode using pygeocoder (Google Geocoding API V3 without key, if several locations are returned, script chooses the first one in the list), then combine permits for the exact same geolocation (sometimes addresse is written differently for different permits, but the geolocation returned by Google is the same).

Mapping:

We use cartoDB for the mapping. We are using the CartoDB.js API for filtering. We are looking into their SQL API to update data automatically. 

[To view default map](http://childcaremap.github.io/NYCdaycare/)

GitHub page is maintained in seperate gh-pages branch (now the default) which gets updated with master but not vice-versa.

Jekyll with a modified single page responsive theme Solo. Docs are here https://github.com/chibicode/solo. Thanks to Shu Uesugi (<a href="http://twitter.com/chibicode">Twitter</a>/<a href="http://github.com/chibicode">GitHub</a>/<a href="https://plus.google.com/110325199858284431541?rel=author">G+</a>).

=====================
License:

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
