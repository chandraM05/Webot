import nltk
from nltk import word_tokenize, pos_tag

wedding_type=['hindu','christian','muslim']
synonyms_event={}
synonyms_event['wedding']=['marriage','wedding' , 'nuptial', 'matrimony']
synonyms_event['reception']=['reception']
synonyms_event['sangeet']=['sangeet']
synonyms_event['mehendi']=['mehendi']
synonyms_event['engagement']=['engagement']

synonyms_service={}
synonyms_service['venue']=['place of wedding','venue','place of marriage','place of nuptials','place']
synonyms_service['dj']=['jockey','dj','music','djs','jockies']
synonyms_service['card']=['card','invitation']
synonyms_service['cake']=['cake','pastry']
synonyms_service['photo']=['photo','photography','shutterbug','photographer']
synonyms_service['catering']=['caterer','food','buffet','dinner','lunch','catering']
synonyms_service['video']=['video','coverage','videography']
synonyms_service['makeup']=['makeup','parlour','beautician']
synonyms_service['decoration']=['decoration','decorator']
synonyms_service['jewellery']=['jewellery','bangel','necklace','ring']
synonyms_service['transportaion']=['bus','car','taxi','transportation','flights','aeroplanes','transport']
synonyms_service['choreographer']=['choreographer']
synonyms_service['accessories']=['accessories','purse','shoe']
synonyms_service['accomodation']=['accomodation','stay','hotel','lodge']
synonyms_service['trousseau']=['gift','trousseau','wrapper']
synonyms_service['clothing']=['clothing','wear','shopping malls','shopping']
# check its brid,groom else family

cities=['delhi','mumbai','kolkata','chennai','pune','bangalore','hyderabad','goa','jaipur','chandigarh','ahmedabad','agra','ambala','amritsar','aurangabad','bhopal','bhubaneswar','coimbatore','dehradun','guwahati','indore','jaisalmer','jalandhar','jodhpur','kerala','lonavala','lucknow','ludhiana','madurai','mangalore','mussoorie','mysore','nagpur','nashik','patiala','pushkar','raipur','ranchi','shimla','siliguri','silvassa','srinagar','surat','udaipur','vodadara','varanasi','visakhapatanam','puri','ooty','coorg','pondicherry','kanpur','allahabad']
month=['jan','feb','march','april','may','june','july','aug','sep','oct','nov','dec']


def get_table(service) :
	event_table={}
	event_table['venue']='venues'
	event_table['dj']='djs'
	event_table['card']='cards'
	event_table['cake']='cakes'
	event_table['photo']='photographers'
	event_table['catering']='catering'
	event_table['makeup']='makeup'
	event_table['decoration']='decorators'
	event_table['jewellery']='jewellery'
	event_table['choreographer']='choreographers'
	event_table['accessories']='accessories'
	event_table['trousseau']='trousseau'
	event_table['bridal']='bwear'
	event_table['groom']='gwear'
	return event_table[service]

def get_vendor(query,msg) :
	pos_tokens=pos_tag(word_tokenize(query))
	# print pos_tokens
	for i in range(0,len(pos_tokens)) :
		# print pos_tokens[i][0],pos_tokens[i][1]
		if "NN" in pos_tokens[i][1] or "NNS" in pos_tokens[i][1]:
			vendor= pos_tokens[i][0].strip()
			l=msg.split("\n")
			for i in range(0,len(l)) :
				if vendor in l[i] :
					if len(vendor)>2 :
						# print l[i]
						return l[i].split(":")[1].split("Ratings")[0]

def extract_info(query) :
	pos_tokens=pos_tag(word_tokenize(query))
	# print pos_tokens

	ext_details={}
	ext_details['event']=""
	ext_details['location']=""
	ext_details['wedding_type']=""
	ext_details['budget']=-1
	ext_details['service']=""
	ext_details['date']=""

	for i in range(0,len(pos_tokens)) :
		# print pos_tokens[i][0],pos_tokens[i][1]
		flag=0
		if "NN" in pos_tokens[i][1] :
			
			for j in range(0,len(cities)) :
				if cities[j] in pos_tokens[i][0] :
					flag=1
					ext_details['location']=pos_tokens[i][0].strip()
					break
			if flag == 0 :
				for key in synonyms_event :
					if flag == 0 :
						for k in range(0,len(synonyms_event[key])) :
							if synonyms_event[key][k] in pos_tokens[i][0] :
								flag=1
								ext_details['event']=key
								break
					else :
						break
			if flag == 0 :
				for key in synonyms_service :
					if flag == 0 :
						for k in range(0,len(synonyms_service[key])) :
							# print synonyms_service[key][k]
							if synonyms_service[key][k] in pos_tokens[i][0] :
								flag=1
								ext_details['service']=key
								break
					else :
						break
			if flag == 0 :
				for type_w in range(0,len(wedding_type)):
					if wedding_type[type_w] in pos_tokens[i][0] :
						flag=1
						ext_details['wedding_type']=pos_tokens[i][0].strip()
			if flag == 0 :
				for k in range(0,len(month)) :
					if month[k] in pos_tokens[i][0] :
						flag = 1
						ext_details['date']="--/"+str(k+1)+"/2017"


		elif "CD" in pos_tokens[i][1] :
			if "/" in pos_tokens[i][0] :
				ext_details['date']=pos_tokens[i][0].strip()
			else :
				cost=pos_tokens[i][0].strip()
				cost=cost.replace("k","000")
				cost=cost.replace("m","000000")
				cost=cost.replace(" ","")
				ext_details['budget']=int(cost)
		elif "VBN" in pos_tokens[i][1] :
			if "dj" in pos_tokens[i][0] :
				flag=1
				ext_details['service']="dj"

	# print "extraction done"
	# for keys in ext_details :
	# 	print keys ,":",ext_details[keys]
	return ext_details
