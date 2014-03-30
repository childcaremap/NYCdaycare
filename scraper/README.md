==- WHAT IS IT? -==

Scraper for data on https://a816-healthpsi.nyc.gov/ChildCare/ChildCareList.do. Currently it retrieves center name + address from the list view and borough and permit no. from individual view.

==- NOTICE -==

1. Browser based only. Cannot be run from commandline or with cron.
2. Please respect the 5 seconds interval so as not to hammer the https://a816-healthpsi.nyc.gov site, and don't run this every day

==- USAGE -==

1. Upload files to your server of local environment
2. Make sure cookie.txt and daycarenyc.csv are writable
3. Edit config.inc.php to set the script reload delay (please use a minimum of 5 seconds) and fill in your DB settings
4. Import centers.sql to your database
5. If you want to have lat/long geocoding data, you need a Google Geocoding API key.
	1. Visit the APIs console at https://code.google.com/apis/console and log in with your Google Account.
	2. Click the Services link from the left-hand menu in the APIs Console, then activate the Geocoding API service.
	3. Once the service has been activated, your API key is available from the API Access page, in the Simple API Access section. Geocoding API applications use the Key for server apps.
5. In your browser open daycare.php -> keep it open until you see "Finished". It will reload every 5 seconds (or whatever you put in your config) until it has retrieved all the pages.