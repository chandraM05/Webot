

class Events:
	location=''
	bugdet=0
	def __init__(self, location, budget):
		self.venue=['','']
		self.card=['','']
		self.cake=['','']
		self.dj=['','']
		self.photographer=['','']
		self.catering=['','']
		self.videography=['','']
		self.mehendi=['','']
		self.clothing=['','']
		self.makeup=['','']
		self.jewellery=['','']
		self.transportation=['','']
		self.choreographer=['','']
		self.accessorie=['','']
		self.accomodation=['','']
		self.trousseau=['','']
		self.services ={'venue':-1,'cards':-1,'cakes':-1,'djs':-1,'photographers':-1,'catering':-1,'videography':-1,'mehendi':-1,
			'clothing':-1,'makeup':-1,'jewellery':-1,'transportation':-1,
			'choreographers':-1,'accessories':-1,'accomodation':-1,'trousseau':-1
		}

	def printdetails(self):
		print "venues",self.venue[0]," ",self.venue[1]
		print "cards",self.card[0], " ",self.card[1]
		print "cakes",self.cake[0]," ",self.cake[1]
		print "djs" ,self.dj[0]," ",self.dj[1]
		print "photographers",self.photographer[0]," ",self.photographer[1]
		print "catering",self.catering[0]," ",self.catering[1]
		print "videography",self.videography[0]," ",self.videography[1]
		print "mehendi",self.mehendi[0]," ",self.mehendi[1]
		print "makeup",self.makeup[0]," ",self.makeup[1]
		print "jewellery",self.jewellery[0]," ",self.jewellery[1]
		print "sangeet_choreographers",self.choreographer[0]," ",self.choreographer[1]
		print "accessories",self.accessorie[0]," ",self.accessorie[1]
		print "hotel_bookings",self.accomodation[0]," ",self.accomodation[1]
		print "clothing",self.clothing[0]," ",self.clothing[1]
		print "trousseau_packers",self.trousseau[0]," ",self.trousseau[1]