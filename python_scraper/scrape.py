import time
time.clock()
import csv
import mechanize
from lxml import html, etree
#from StringIO import StringIO

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

output_file = open("output.csv","wb")
header = ["Site ID","Center Name","Permit Holder","Address","Borough","Zip Code","Phone","Permit Number","Permit Expiration Date","Permit Status","Age Range","Maximum Capacity","Certified to Administer Medication","Site Type"]
writer = csv.writer(output_file)
writer.writerow(header)


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
        #tree = etree.parse(StringIO(page2), parser)
        #print etree.tostring(tree.getroot(), pretty_print=True)
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
        writer.writerow(row)

    offset = offset + 10

output_file.close()
time_elapsed = time.clock()
print [str(time_elapsed)+" seconds"]
print [str(time_elapsed/60)+" minutes"]
