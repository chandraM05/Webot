import frame



def context_manager(ext_details,global_event,global_service, events_dic) :

	# print ext_details ," context manager "

	if ext_details['event']!='':
		global_event=ext_details['event']
		events_dic[ext_details['event']]=frame.Events('','')
		# print "object"
	if ext_details['budget']!='':
		global_budget=ext_details['budget']
	if ext_details['service']!='':
		global_service=ext_details['service']
	if global_service!='':
		events_dic[global_event].services[global_service]=1

	chckflg=0
	if events_dic[global_event].services["venue"]==1:
		if ext_details["location"]!='': 
			chckflg=1
			events_dic[global_event].venue[0]=ext_details["location"]
			if events_dic[global_event].venue[1]!='':
				events_dic[global_event].services["venue"]=2
	elif events_dic[global_event].services["cards"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].cards[0]=ext_details["location"]
			if events_dic[global_event].cards[1]!='':
				events_dic[global_event].services["cards"]=2
	elif events_dic[global_event].services["cakes"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].cakes[0]=ext_details["location"]
			if events_dic[global_event].cakes[1]!='':
				events_dic[global_event].services["cakes"]=2
	elif events_dic[global_event].services["djs"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].djs[0]=ext_details["location"]
			if events_dic[global_event].djs[1]!='':
				events_dic[global_event].services["djs"]=2
	elif events_dic[global_event].services["photographers"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].photographers[0]=ext_details["location"]
			if events_dic[global_event].photographers[1]!='':
				events_dic[global_event].services["photographers"]=2
	elif events_dic[global_event].services["catering"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].catering[0]=ext_details["location"]
			if events_dic[global_event].catering[1]!='':
				events_dic[global_event].services["catering"]=2
	elif events_dic[global_event].services["videography"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].videography[0]=ext_details["location"]
			if events_dic[global_event].videography[1]!='':
				events_dic[global_event].services["videography"]=2
	elif events_dic[global_event].services["mehendi"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].mehendi[0]=ext_details["location"]
			if events_dic[global_event].mehendi[1]!='':
				events_dic[global_event].services["mehendi"]=2
	elif events_dic[global_event].services["clothing"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].bridal_groom_wear[0]=ext_details["location"]
			if events_dic[global_event].bridal_groom_wear[1]!='':
				events_dic[global_event].services["bridal_groom_wear"]=2
	elif events_dic[global_event].services["makeup"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].bridal_makeup[0]=ext_details["location"]
			if events_dic[global_event].bridal_makeup[1]!='':
				events_dic[global_event].services["bridal_makeup"]=2
	elif events_dic[global_event].services["jewellery"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].jewellery[0]=ext_details["location"]
			if events_dic[global_event].jewellery[1]!='':
				events_dic[global_event].services["jewellery"]=2
	elif events_dic[global_event].services["transportation"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].Transportation[0]=ext_details["location"]
			if events_dic[global_event].Transportation[1]!='':
				events_dic[global_event].services["Transportation"]=2
	elif events_dic[global_event].services["choreographers"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].sangeet_choreographers[0]=ext_details["location"]
			if events_dic[global_event].sangeet_choreographers[1]!='':
				events_dic[global_event].services["choreographers"]=2
	elif events_dic[global_event].services["accessories"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].accessories[0]=ext_details["location"]
			if events_dic[global_event].accessories[1]!='':
				events_dic[global_event].services["accessories"]=2
	elif events_dic[global_event].services["accomodation"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].hotel_bookings[0]=ext_details["location"]
			if events_dic[global_event].hotel_bookings[1]!='':
				events_dic[global_event].services["hotel_bookings"]=2
	elif events_dic[global_event].services["trousseau"]==1:
		if ext_details["location"]!='':
			chckflg=1
			events_dic[global_event].trousseau_packers[0]=ext_details["location"]
			if events_dic[global_event].trousseau_packers[1]!='':
				events_dic[global_event].services["trousseau"]=2
		# print global_event.key[0]
	if chckflg==1:
		events_dic[global_event].location=ext_details["location"]
	

	chckflg=0
	if events_dic[global_event].services["venue"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].venue[1]=ext_details["budget"]
			if events_dic[global_event].venue[0]!='':
				events_dic[global_event].services["venue"]=2
	elif events_dic[global_event].services["cards"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].cards[1]=ext_details["budget"]
			if events_dic[global_event].cards[0]!='':
				events_dic[global_event].services["cards"]=2
	elif events_dic[global_event].services["cakes"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].cakes[1]=ext_details["budget"]
			if events_dic[global_event].cakes[0]!='':
				events_dic[global_event].services["cakes"]=2
	elif events_dic[global_event].services["djs"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].djs[1]=ext_details["budget"]
			if events_dic[global_event].djs[0]!='':
				events_dic[global_event].services["djs"]=2
	elif events_dic[global_event].services["photographers"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].photographers[1]=ext_details["budget"]
			if events_dic[global_event].photographers[0]!='':
				events_dic[global_event].services["photographers"]=2
	elif events_dic[global_event].services["catering"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].catering[1]=ext_details["budget"]
			if events_dic[global_event].catering[0]!='':
				events_dic[global_event].services["catering"]=2
	elif events_dic[global_event].services["videography"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].videography[1]=ext_details["budget"]
			if events_dic[global_event].videography[0]!='':
				events_dic[global_event].services["videography"]=2
	elif events_dic[global_event].services["mehendi"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].mehendi[1]=ext_details["budget"]
			if events_dic[global_event].mehendi[0]!='':
				events_dic[global_event].services["mehendi"]=2
	elif events_dic[global_event].services["clothing"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].bridal_groom_wear[1]=ext_details["budget"]
			if events_dic[global_event].bridal_groom_wear[0]!='':
				events_dic[global_event].services["clothing"]=2
	elif events_dic[global_event].services["makeup"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].bridal_makeup[1]=ext_details["budget"]
			if events_dic[global_event].bridal_makeup[0]!='':
				events_dic[global_event].services["makeup"]=2
	elif events_dic[global_event].services["jewellery"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].jewellery[1]=ext_details["budget"]
			if events_dic[global_event].jewellery[0]!='':
				events_dic[global_event].services["jewellery"]=2
	elif events_dic[global_event].services["transportation"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].Transportation[1]=ext_details["budget"]
			if events_dic[global_event].Transportation[0]!='':
				events_dic[global_event].services["transportation"]=2
	elif events_dic[global_event].services["choreographers"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].sangeet_choreographers[1]=ext_details["budget"]
			if events_dic[global_event].sangeet_choreographers[0]!='':
				events_dic[global_event].services["choreographers"]=2
	elif events_dic[global_event].services["accessories"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].accessories[1]=ext_details["budget"]
			if events_dic[global_event].accessories[0]!='':
				events_dic[global_event].services["accessories"]=2
	elif events_dic[global_event].services["accomodation"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].hotel_bookings[1]=ext_details["budget"]
			if events_dic[global_event].hotel_bookings[0]!='':
				events_dic[global_event].services["accomodation"]=2
	elif events_dic[global_event].services["trousseau"]==1:
		if ext_details["budget"]!=-1: 
			chckflg=1
			events_dic[global_event].trousseau_packers[1]=ext_details["budget"]
			if events_dic[global_event].trousseau_packers[0]!='':
				events_dic[global_event].services["trousseau"]=2
	if chckflg==1:
		events_dic[global_event].budget=ext_details["budget"]

	# print "class"
	# global_event.printdetails()

	# events_dic["reception"].location='pune'
	# print events_dic["reception"].location
	if ext_details["service"]=="" :
		for key,value in events_dic[global_event].services.iteritems() :
			if value == 1:
				ext_details["service"] = key
				break
	if ext_details["event"] == "" :
		ext_details["event"] = global_event
	if ext_details["location"] == "" :
		ext_details["location"] = events_dic[global_event].location
	if ext_details["budget"] == 0 :
		ext_details["budget"] = events_dic[global_event].budget
	if ext_details["service"] == "" :
		ext_details["service"] = global_service

	# if global_service!='':
	# 	incomplete(global_event,global_service,events_dic)

	return ext_details,global_event,global_service, events_dic

def incomplete(global_event,global_service,events_dic,msg):
	# inflg2=0	
	ultimate_break=0
	for key,value in events_dic.iteritems():
		# print "check1"
		inflg2=1
		if value!=0:
			flg=0
			inflg=0
			for key1,value1 in events_dic[global_event].services.iteritems():
				# print "check2"
				if value1==1:
					k=events_dic[global_event]
					# for attr, value2 in k.__dict__.iteritems():
					if 1 == 1 :	
						inflg=1
						if msg != "" :
							print "				Hi are you busy"
							ultimate_break = 1
							break;
						elif attr==key1:
							print "				would you like to avail ",attr
							# if value2[0]=='':
							# 	print "what is location"
							# else:
							# 	print "what is budget"
							# 	flg=1
							ultimate_break = 1
							break;
			if  ultimate_break == 1 :
				break;
			if inflg==0 :
						print "				Hi which service you want to avail !!!"
						ultimate_break = 1
						break;

	# if inflg2==0 :
			# print "Hi want to plan any event !!!"
					