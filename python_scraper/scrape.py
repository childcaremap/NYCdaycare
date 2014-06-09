import time
time.clock()
import csv
import mechanize
from lxml import html, etree
#from StringIO import StringIO
from lxml.html.soupparser import fromstring
import re

offset = 0
request = mechanize.Request("https://a816-healthpsi.nyc.gov/ChildCare/SearchAction2.do?pager.offset=" + str(offset))
response = mechanize.urlopen(request)

cj = mechanize.CookieJar()
cj.extract_cookies(response, request)

forms = mechanize.ParseResponse(response, backwards_compat=False)
response.close()
form = forms[0]
form.set_all_readonly(False)
form["getNewResult"] = "true"
page = mechanize.urlopen(form.click()).read()

tree = html.fromstring(page)
pages = tree.xpath('.//a[@class="pager"]')
offsetstring = pages[len(pages)-1].get('href')
maxpage = offsetstring[offsetstring.index('=')+1:len(offsetstring)]

outfile_basic = open("BasicInfo.csv","wb")
header = ["Site ID","Center Name","Permit Holder","Address","Borough","Zip Code","Phone","Permit Number","Permit Expiration Date","Permit Status","Age Range","Maximum Capacity","Certified to Administer Medication","Site Type"]
writer_basic = csv.writer(outfile_basic)
writer_basic.writerow(header)

outfile_insp = open("InspectionInfo.csv","wb")
header = ["Site ID","Visit Date","Regulation Summary","Violation Category","Code-Sub-Section","Violation Status"]
writer_insp = csv.writer(outfile_insp)
writer_insp.writerow(header)

outfile_summ = open("InspectionSummaries.csv","wb")
header = ["Site ID","Visit Date","Visit Type","Summary"]
writer_summ = csv.writer(outfile_summ)
writer_summ.writerow(header)

while offset <= int(maxpage):
    print "Offset: " + str(offset)
    request = mechanize.Request("https://a816-healthpsi.nyc.gov/ChildCare/SearchAction2.do?pager.offset=" + str(offset))
    cj.add_cookie_header(request)
    response = mechanize.urlopen(request)
    page = response.read()

    #with open("output.txt","wb") as output_file:
    #	output_file.write(page)

    tree = html.fromstring(page)
    links = tree.xpath('.//td[@class="cell_leftborder"]/a')

    for link in links:
        onclickcommand =  link.get('onclick')
        siteid = onclickcommand.split('redirectHistory(')[1]
        siteid.index('"); return false')
        siteid = siteid[1:siteid.index('"); return false')]
        print siteid

        request2 = mechanize.Request("https://a816-healthpsi.nyc.gov/ChildCare/WDetail.do","linkPK="+str(siteid))
        cj.add_cookie_header(request2)
        response2 = mechanize.urlopen(request2)
        page2 = response2.read()
        #with open("output2.txt","wb") as output_file:
        #	output_file.write(page2)

        #parser = etree.HTMLParser()
        #tree2 = etree.parse(StringIO(page2), parser)
        #print etree.tostring(tree2.getroot(), pretty_print=True)
        tree = html.fromstring(page2)
        lines = tree.xpath('.//td[@class="cell_border_rightbottomtop_noback"]|.//td[@class="cell_border"]')
        row = []
        row.append(str(siteid))
        for i, line in enumerate(lines):
            if i == 8:
                #print line.xpath('./a')[0].text
                #print etree.tostring(line)
                row.append(line.xpath('./a')[0].text.encode("ascii","ignore"))
            else:
                #print line.text
                row.append(line.text.encode("ascii","ignore"))
        #print row
        writer_basic.writerow(row)
        #page is broken html, need beautifulsoup parser to get at health inspections
        root = html.soupparser.fromstring(page2)
        #output_btree = open("output_btree.html","wb")
        #output_btree.write(etree.tostring(root, pretty_print=True).strip())
        #print(etree.tostring(root, pretty_print=True).strip())
        
        tables = root.xpath('.//table[@style="width:100%"]')
        try:
            inspection_info = root.xpath('.//table/tr/td[@class="alt_border"]')[0].text
            match = re.search('DATE:',inspection_info)
            date = inspection_info[match.end()+1:-2].encode("ascii","ignore")

            row_summ = [siteid,date]
            inspection_type = inspection_info[2:match.start()-1].replace(u'\xa0',u' ').encode("ascii")
            row_summ.append(inspection_type)
            inspection_summ = root.xpath('.//a[@class="headline"][2]')[0].tail.strip()
            row_summ.append(inspection_summ)
            writer_summ.writerow(row_summ)

            regulations = tables[1].xpath('.//td[@class="cell_leftborder"]')
            for i,reg in enumerate(regulations):
                row_inspect = []
                row_inspect.append(siteid)
                row_inspect.append(date)
                row_inspect.append(reg.text.encode("ascii","ignore"))
                details = tables[1].xpath('.//td[@class="cell_leftborder"]['+str(i+1)+']/following::td[@class="cell_border"][1]')
                try:
                    row_inspect.append(details[0].xpath('./a')[0].text.encode("ascii","ignore"))
                except:
                    row_inspect.append(details[0].text.encode("ascii","ignore"))
                details = tables[1].xpath('.//td[@class="cell_leftborder"]['+str(i+1)+']/following::td[@class="cell_border"][2]')
                row_inspect.append(details[0].text.encode("ascii","ignore"))
                details = tables[1].xpath('.//td[@class="cell_leftborder"]['+str(i+1)+']/following::td[@class="cell_border"][3]')
                row_inspect.append(details[0].text.encode("ascii","ignore"))
                writer_insp.writerow(row_inspect)
        except:
            row_summ = [siteid]
            row_summ.append('No visit found in database.')
            row_summ.append('')
            row_summ.append('')
            writer_summ.writerow(row_summ)

    offset = offset + 10

outfile_basic.close()
outfile_insp.close()
outfile_summ.close()
time_elapsed = time.clock()
print [str(time_elapsed)+" seconds"]
print [str(time_elapsed/60)+" minutes"]