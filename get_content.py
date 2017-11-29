import contextlib
import selenium.webdriver as webdriver
import lxml.html as LH
import lxml.html.clean as clean
import re

f = open("../links/service_link","r")
primary_data = f.readlines()
f.close()

# control =1
for services in primary_data :
# services = "wedding-videography		https://www.wedmegood.com/vendors/all/wedding-videography/"
# if control == 1 :
	service=services.split("	")[0]
	
	f= open("../links/"+service,'r')
	vendors=f.readlines()
	f.close()

	with open("../data/"+service,'a+') as f1:

		print service

		for vendor in range(38,len(vendors)) :
			seed_link = vendors[vendor]
			print seed_link

			with contextlib.closing(webdriver.Firefox()) as browser:
			    browser.get(seed_link)
			    content=browser.page_source
			    cleaner=clean.Cleaner()
			    content=cleaner.clean_html(content)    
			    # with open('trash.html','w') as f:
			    # 	f.write(content.encode('utf-8'))
			    # 	f.close()

			# f = open("trash.html","r")
			# trash_data = f.readlines()
			# f.close()
			# stri=""
			# for i in trash_data :
			# 	stri=stri+i

			name=seed_link.split("/")[-2]

			tree = LH.fromstring(unicode(content.encode('utf-8'), "utf-8"))

			# extracting city
			temp = tree.xpath("//div[@id='venueOverviewDetail']//h1//span//a//text()")
			city=""
			for i in temp :
				city=city+i
			city=re.sub('[^a-zA-Z-_*.]', '', city)

			# extracting ratings
			temp1 = tree.xpath("//div[@id='venueOverviewDetail']//a//div//p//span//text()")
			# print temp1,vendor
			rating=temp1[0].encode('utf-8')

			# extracting reviews
			review=""
			for temp2 in tree.xpath("//div[@class='isDesktop']//section//p[@class='review-text']//text()") :
				review=review+"***"+temp2.encode('utf-8')

			temp3 = tree.xpath("//div[@id='starting-price-div']//p//text()") 
			price1=""
			for i in temp3 :
				price1=price1+i
			# price1=re.sub('[^0-9 ]', '', price1)
			# price=price1.split("-")[-1]
			price =re.sub('[^0-9 ]', '', price1)

			# price=""
			print name,city,rating,price,vendor
			f1.write(name+" ! "+city+" ! "+rating+" ! "+price+" ! "+review+">>>"+"\n")
			# break
		f1.close()
	# break