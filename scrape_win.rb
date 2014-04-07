require 'rubygems'
require 'mechanize'
require 'csv'

agent1 = Mechanize.new
agent2 = Mechanize.new

output = File.new("output.csv","w")
output.print("Center Name,Permit Holder,Address,Borough,Zip Code,Phone,Permit Number,Permit Expiration Date,Permit Status,Age Range,Maximum Capacity,Certified to Administer Medication,Site Type")
output.print("\n")

offset = 0

#following lines only necessary for Windows machines
cert_store = OpenSSL::X509::Store.new
cert_store.add_file 'cacert.pem'
agent1.cert_store = cert_store
agent2.cert_store = cert_store

page = agent1.post 'https://a816-healthpsi.nyc.gov/ChildCare/SearchAction2.do?pager.offset=' + offset.to_s, 'getNewResult' => true

pages = page.search('.//a[@class="pager"]')
offsetstring = pages[pages.length-1][@name="href"]
maxpage = offsetstring[offsetstring.index('=')+1,offsetstring.length-1]
maxpage.to_i

while offset <= maxpage.to_i do
	puts "Offset: " + offset.to_s

	page = agent1.post 'https://a816-healthpsi.nyc.gov/ChildCare/SearchAction2.do?pager.offset=' + offset.to_s, 'getNewResult' => true

	agent1.cookie_jar.save_as 'cookies', :session => true, :format => :yaml

	#sleep(5)

	links = page.search('.//td[@class="cell_leftborder"]/a')

	links.each do |link|
		
		id = link.to_s()
		id = id.split('redirectHistory(')[1]
		id = id[0,10]
		id = id.scan(/"([^"]*)"/)
		puts id

		agent2.cookie_jar = agent1.cookie_jar

		idString = 'linkPK=' + id[0][0].to_s
		puts idString

		page2 = agent2.post 'https://a816-healthpsi.nyc.gov/ChildCare/WDetail.do', idString ,({'Content-Type' => 'application/x-www-form-urlencoded'})
		
		#sleep(5)

		#rows = page2.search('.//table[4]/tr/td[@class="cell_border"]')
		#rows = page2.search('.//table[4]/tr/td[@class="cell_border_rightbottomtop_noback"]')
		#for some reason, info is not in table number 4 anymore, but in table number 1. platform issue or did they change the webpage?
		rows = page2.search('.//table[1]/tr/td[@class="cell_border"]|.//table[1]/tr/td[@class="cell_border_rightbottomtop_noback"]')

		rows.each do |row|
			puts
			puts row.text
			output.print row.text.gsub(/[^\w\s\-\/]/, "").gsub(/\r?\n|\r/,"")
			output.print(",")

		end

		output.print("\n")
		

	end

offset = offset + 10

end


