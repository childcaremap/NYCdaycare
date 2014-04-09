daycare_scraper
===============

Scrapes data about licensed daycare facilities from the NYC Dept of Mental Hygiene

Approximately 2200 daycares are included on this searchable web portal, but the data are not available in aggregate for download.

This ruby script iterates over each index page (showing 10 listings each), and POSTs to https://a816-healthpsi.nyc.gov/ChildCare/WDetail.do for each one.
The WDetail.do page has a table of information about the daycare.  Mechanize is used to scrape this page, and export to CSV.

Born of a community need on the BetaNYC discussion group.  
http://www.meetup.com/betanyc/messages/archive/
