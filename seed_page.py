import requests
import urllib2
from lxml import html
import lxml.html

vendor_type = {}

seed_link = 'https://www.wedmegood.com'
response = requests.get(seed_link)
tree = html.fromstring(response.text)


f =  open("../links/link_type1","w")
for link in tree.xpath('//div//a/@href') :
	temp=link.split("/")
	if len(temp)== 5 and temp[-1]=="":
		if temp[3] not in vendor_type :
			vendor_type[temp[3]] = seed_link+'/vendors/all/'+temp[3]
			f.write(temp[3]+"		"+seed_link+'/vendors/all/'+temp[3]+"/\n")
# print vendor_type ,len(vendor_type)
vendor_type['family-makeup'] = seed_link+'/vendors/all/family-makeup/'
vendor_type['planners'] = seed_link+'/vendors/all/planners/'
f.write('family-makeup'+"		"+seed_link+'/vendors/all/family-makeup/'+"\n")
f.write('planners'+"		"+seed_link+'/vendors/all/planners/'+"\n")
f.close()

#--------------------------------------------------------------------------------------------------------