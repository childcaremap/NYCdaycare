require 'rubygems'
require 'mechanize'
require 'csv'

agent1 = Mechanize.new
agent2 = Mechanize.new

output = File.new("output2.csv","w")
output.print("centerName,permitHolder,address,borough,phone,zipCode,permitNumber,permitExpirationDate,permitStatus,ageRange,maximumCapacity,certifiedToAdministerMedication,siteType")
output.print("\n")

offset = 0

while offset < 2300 do
	puts "Offset: " + offset.to_s

	page = agent1.post 'https://a816-healthpsi.nyc.gov/ChildCare/SearchAction2.do?pager.offset=' + offset.to_s, 'getNewResult' => true

	agent1.cookie_jar.save_as 'cookies', :session => true, :format => :yaml

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

		#rows = page2.search('.//table[4]/tr/td[@class="cell_border"]')
		rows = page2.search('.//table[4]/tr/td[@class="cell_border"]|.//table[4]/tr/td[@class="cell_border_rightbottomtop_noback"]')

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


